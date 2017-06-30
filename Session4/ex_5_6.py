import requests
from bs4 import BeautifulSoup

import json


def get_video_links():
    res = requests.get('http://video.vnexpress.net')
    soup = BeautifulSoup(res.content, 'html.parser')

    list_videos_div = soup.find(name='div', attrs={'class': 'list_video hidden_list width_common'})

    links = list()
    for vd in list_videos_div.find_all(name='div', attrs={'class': 'each_element item_video'}):
        data_extend_attr = vd.get('data-extend')
        link = json.loads(data_extend_attr).get('s360')

        links.append(link)

    return links


def download_video(link):
    paths = link.split('/')
    fn = paths[-1]  # Take the last path segment in URL

    fw = open(fn, mode='wb')
    res = requests.get(link)
    fw.write(res.content)


links = get_video_links()

for link in links:
    print(link)

# Download 5 videos
for link in links[:5]:
    download_video(link)
