import requests
from bs4 import BeautifulSoup

url = "https://www.joongbu.ac.kr/board.es?mid=a10301000000&bid=0007&act=view&list_no=296090&tag=&nPage=1"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
targetbox = soup.find('div', attrs={"class": "tb_contents"})
targetbox2 = targetbox.find('p')

if targetbox2.find('img'):
    print("이미지 파일입니다")
else:
    # 처리할 로직 작성
    # 예: 텍스트로 구성된 경우의 처리
    paragraphs = targetbox2.find_all('p')
    for paragraph in paragraphs:
        content = paragraph.get_text().strip()
        print(content)
