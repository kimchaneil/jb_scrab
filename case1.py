import csv
import requests
from bs4 import BeautifulSoup
import os

filename = "case1_content.csv"

if os.path.exists(filename):
    with open(filename, "w", encoding="utf-8-sig", newline=""):
        pass

url = "https://www.joongbu.ac.kr/board.es?mid=a10301000000&bid=0007&act=view&list_no=296163&tag=&nPage=1"

f = open(filename, "a", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

columns_name = ["content"]
writer.writerow(columns_name)

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
targetbox = soup.find('div', attrs={"class": "tb_contents"})
paragraphs = targetbox.find_all('p', attrs={"class": "0"})

for paragraph in paragraphs:
    targets = paragraph.find_all('span')
    print(targets)
    content = ''

    for target in targets:
        bold = target.get_text()
        content += bold + ' '

    print(content)
    data = [content]
    writer.writerow(data)

f.close()
