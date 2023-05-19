import csv
import requests
from bs4 import BeautifulSoup
import os

filename = "case2_content.csv"

if os.path.exists(filename):
    with open(filename, "w", encoding="utf-8-sig", newline=""):
        pass

url = "https://www.joongbu.ac.kr/board.es?mid=a10301000000&bid=0007&act=view&list_no=294901&tag=&nPage=3"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
targetbox = soup.find('div', attrs={"class": "tb_contents"})
paragraphs = targetbox.find_all('p')

with open(filename, "a", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["content"])  # CSV 파일의 헤더 쓰기

    for paragraph in paragraphs:
        content = paragraph.get_text().strip()  # p 요소의 텍스트 추출
        writer.writerow([content])  # CSV 파일에 한 줄씩 쓰기
