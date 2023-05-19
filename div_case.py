import requests
from bs4 import BeautifulSoup
import os
import csv

url = "https://www.joongbu.ac.kr/board.es?mid=a10301000000&bid=0007&act=view&list_no=294901&tag=&nPage=3"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
targetbox = soup.find('div', attrs={"class": "tb_contents"})
targetbox_p = targetbox.find('p')

if targetbox_p.find('span'):
    filename = "case1_content.csv"
    if os.path.exists(filename):
        with open(filename, "w", encoding="utf-8-sig", newline=""):
            pass
    f = open(filename, "a", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)
    columns_name = ["content"]
    writer.writerow(columns_name)
    print("Case 1: tb_content -> p -> span")
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
elif targetbox_p.find('img'):
    print("Case 3: tb_content -> p -> img")
    print("이미지 파일입니다")

else:
    print("Case 2: tb_content -> p")
    filename = "case2_content.csv"
    if os.path.exists(filename):
        with open(filename, "w", encoding="utf-8-sig", newline=""):
            pass
    paragraphs = targetbox.find_all('p')
    with open(filename, "a", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["content"])  # CSV 파일의 헤더 쓰기

        for paragraph in paragraphs:
            content = paragraph.get_text().strip()  # p 요소의 텍스트 추출
            writer.writerow([content])  # CSV 파일에 한 줄씩 쓰기
