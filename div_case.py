import requests
from bs4 import BeautifulSoup
import os
import csv
import pymongo
import subprocess
client = pymongo.MongoClient("mongodb+srv://chaneil2:k8909@jbchat.abd4i2a.mongodb.net/")
db = client["chat"]
collection = db["titles"]
urls = []
documents = collection.find({}, {"url": 1})
for doc in documents:
    urls.append(doc["url"])
num_urls = len(urls)
#print(urls)
for i in range(num_urls):
    url = urls[i]
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    targetbox = soup.find('div', attrs={"class": "tb_contents"})
    if targetbox:
        targetbox_p = targetbox.find('p')

        if targetbox_p.find('span'):
            filename = "case1_content.csv"
            if os.path.exists(filename):
                with open(filename, "w", encoding="utf-8-sig", newline=""):
                    pass
            f = open(filename, "a", encoding="utf-8-sig", newline="")
            writer = csv.writer(f)
            url_name = ["url"]
            writer.writerow(url_name)
            writer.writerow([url])
            columns_name = ["content"]
            #data = [url]
            #writer.writerow(data)
            print("Case 1: tb_content -> p -> span")
            content = ''
            paragraphs = targetbox.find_all('p', attrs={"class": "0"})
            for paragraph in paragraphs:
                targets = paragraph.find_all('span')
                #print(targets)
                #content = ''

                for target in targets:
                    bold = target.get_text()
                    content += bold + ' '
                #print(content)
                data = [content]
            writer.writerow(columns_name)
            writer.writerow([content])
            f.close()
            subprocess.run(["python", "./jb_scrab/data_base_case_1.py"])
        elif targetbox_p.find('img'):
            print("Case 3: tb_content -> p -> img")
            filename = "case3_content.csv"
            if os.path.exists(filename):
                with open(filename, "w", encoding="utf-8-sig", newline=""):
                    pass
            with open(filename, "a", encoding="utf-8-sig", newline="") as f:
                writer = csv.writer(f)
                url_name=["url"]
                writer.writerow(url_name)
                writer.writerow([url])
                content_name=["content"]
                writer.writerow(content_name)
                content = 'image file'
                writer.writerow([content])
                f.close()
                subprocess.run(["python", "./jb_scrab/data_base_case_3.py"])

        else:
            print("Case 2: tb_content -> p")
            filename = "case2_content.csv"
            if os.path.exists(filename):
                with open(filename, "w", encoding="utf-8-sig", newline=""):
                    pass
            paragraphs = targetbox.find_all('p')
            with open(filename, "a", encoding="utf-8-sig", newline="") as f:
                writer = csv.writer(f)
                url_name=["url"]
                writer.writerow(url_name)
                writer.writerow([url])  # CSV 파일의 헤더 쓰기
                content = ''
                for paragraph in paragraphs:
                    content += paragraph.get_text().strip() # p 요소의 텍스트 추출
                content_name=["content"]
                writer.writerow(content_name) 
                writer.writerow([content])
                f.close()
                subprocess.run(["python", "./jb_scrab/data_base_case_2.py"])

client.close()
