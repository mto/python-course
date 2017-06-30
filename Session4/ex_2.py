import requests
from bs4 import BeautifulSoup

link = 'http://vnexpress.net/tin-tuc/the-gioi/tu-lieu/hong-kong-sau-20-nam-tro-ve-voi-trung-quoc-3606430.html'

res = requests.get(link)
soup = BeautifulSoup(res.text, 'html.parser')

content_div = soup.find(name='div', attrs={'class': 'fck_detail width_common block_ads_connect'})

for p in content_div.find_all(name='p', attrs={'class': 'Normal'}):
    print(p.text)
