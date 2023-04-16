import requests
from bs4 import BeautifulSoup

url = "https://www.snugarchive.com" # target url
res = requests.get(url)
res.raise_for_status() # 정상 200
soup = BeautifulSoup(res.text,"lxml")


print(soup.head) # HTML 문서의 'head' 태그에 해당하는 내용 출력
#print(type(soup)) # BeautifulSoup 객체의 자료형 출력
#print(soup.body)  # HTML 문서의 'body' 태그에 해당하는 내용 출력
#print(soup.title) # HTML 문서의 'title' 태그 내용 출력
#print(soup.title.name) # HTML 문서의 'title' 태그명 출력 
#print(soup.title.string) # HTML 문서의 'title' 태그를 제외하고 태그 안에 표시되는 텍스트만 출력