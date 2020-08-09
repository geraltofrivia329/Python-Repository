import requests
import bs4

base_url = ('http://testing-ground.scraping.pro/blocks')
res = requests.get(base_url)
soup = bs4.BeautifulSoup(res.text, 'lxml')

names = soup.select(".name")

for name in names:
    print(name.text)
