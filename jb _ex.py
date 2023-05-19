import csv
import requests
from bs4 import BeautifulSoup
import os
x=1
filename = "학사공지 리스트.csv"
if os.path.exists(filename):
    with open(filename,"w",encoding="utf-8-sig",newline=""):
        pass
for x in range(1,4):
    url = "https://www.joongbu.ac.kr/board.es?mid=a10301000000&bid=0007&nPage="+str(x)

    filename = "학사공지 리스트.csv"
    f = open(filename, "a", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    colums_name = ["페이지","번호","제목","url"]

    writer.writerow(colums_name)

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,"lxml")
    targetbox = soup.find('section',attrs={"id":"content_detail"})
    targetbox2 = targetbox.find('div',attrs={"id":"listView"})
    #print(targetbox2)
    if targetbox is not None:
        targets = targetbox2.find_all('a')
        i=1

        for target in targets:
            title=target.get("title")
            turl=target.get("href")
            #print(f"{str(i)}: {title}")
            data = ['page'+str(x),'title:'+str(i),title,'https://www.joongbu.ac.kr'+turl]
            writer.writerow(data)
            i +=1

        with open("targetbox.txt","a",encoding="utf-8-sig") as f:
            f.write(targetbox.prettify())
    else:
        print("목록을 찾을 수 없습니다.")
    x +=1 
    
f.close()