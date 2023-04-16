import csv
import requests
from bs4 import BeautifulSoup
x=1
for x in range(1,4):
    url = "https://www.joongbu.ac.kr/board.es?mid=a10302000000&bid=0008&&nPage="+str(x)

    filename = "학사공지 리스트.csv"
    f = open(filename, "a", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    colums_name = ["번호","제목"]

    writer.writerow(colums_name)

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,"lxml")
    targetbox = soup.find('section',attrs={"id":"content_detail"})
    targetbox2 = targetbox.find('div',attrs={"id":"listView"})
    print(targetbox2)
    if targetbox is not None:
        targets = targetbox2.find_all('a')
        i=1

        for target in targets:
            title=target.get("title")
            print(f"{str(i)}: {title}")
            data = [str(i),title]
            writer.writerow(data)
            i +=1

        with open("targetbox.txt","a",encoding="utf-8-sig") as f:
            f.write(targetbox.prettify())
    else:
        print("목록을 찾을 수 없습니다.")
    
f.close()