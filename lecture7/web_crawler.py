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

if __name__ == "__main__":
    http = urllib3.PoolManager()
    start_url = 'https://coronavirus.health.ny.gov/county-county-breakdown-positive-cases'
    crawler = WebCrawler(start_url, http, 2)
    crawler.get_page_content(start_url, 0)
    print(crawler.contents.keys())
    print("Got content of ", len(crawler.contents), "pages")