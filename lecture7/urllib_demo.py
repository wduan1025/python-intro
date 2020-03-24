import urllib3
http = urllib3.PoolManager()
print(type(http))
URL = 'https://coronavirus.health.ny.gov/county-county-breakdown-positive-cases'
r = http.request('GET', URL)
print(r)
print(r.status)
content = r.data
print(type(content))
content = content.decode('utf-8')
print(type(content))
with open("ny_corona.txt", "w") as f:
    f.write(content)
# print(content)
