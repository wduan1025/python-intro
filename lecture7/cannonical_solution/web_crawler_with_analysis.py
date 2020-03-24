import urllib3
import re
import time

class WebCrawler:
    sleep_time = 0
    max_try = 3
    max_num_urls = 1000

    def __init__(self, initial_url, manager, levels):
        self.initial_url = initial_url
        self.contents = {}
        self.max_recursion_levels = levels
        self.manager = manager
        self.out_links = {}
        self.in_links = {}

    def run(self):
        self.get_page_content(self.initial_url, 0)

    def get_page_content(self, url, recursion_level):
        if recursion_level >= self.max_recursion_levels or url in self.contents:
            return
        r = None
        for i in range(self.max_try):
            try:
                if i > 0:
                    pass
                    # print("Try to send get request to ", url, "for the", i+1, "time")
                r = self.manager.request('GET', url)
                if not r.status == 200:
                    continue
                content = r.data
                if content is None:
                    return
                content = content.decode('utf-8')
                self.contents[url] = content
                if len(self.contents) > self.max_num_urls:
                    return
                out_links = self.get_out_links(content)
                self.analyze_links(url, out_links)
                for link in out_links:
                    self.get_page_content(link, recursion_level+1)
                break
            except KeyboardInterrupt:
                break
            except:
                continue

    # Get links(wrapped by <a> and </a> in html content)
    # returns a list of string, each is a url
    def get_out_links(self, content):
        pattern = r'<a href="(\S+)">'
        urls = re.findall(pattern, content)
        return urls
    
    def analyze_links(self, source_url, target_urls):
        if not source_url in self.out_links:
            self.out_links[source_url] = set()
        for url in target_urls:
            self.out_links[source_url].add(url)
            if not url in self.in_links:
                self.in_links[url] = set()
            self.in_links[url].add(source_url)

    def summarize_links(self):
        out_link_counts = {source:len(targets) for source,targets in sorted(self.out_links.items(), key=lambda item: item[1])}
        in_link_counts = {target:len(sources) for target,sources in sorted(self.in_links.items(), key=lambda item: item[1])}
        return out_link_counts, in_link_counts

if __name__ == "__main__":
    http = urllib3.PoolManager()
    start_url = 'https://coronavirus.health.ny.gov/county-county-breakdown-positive-cases'
    crawler = WebCrawler(start_url, http, 2)
    crawler.get_page_content(start_url, 0)
    print(crawler.contents.keys())
    # print("Got content of ", len(crawler.contents), "pages")
    # print(crawler.edges)
    out_counts, in_counts = crawler.summarize_links()
    print(out_counts)
    print(in_counts)