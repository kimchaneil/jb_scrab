import pandas as pd
from pymongo import MongoClient

# MongoDB 연결 설정
client = MongoClient('mongodb+srv://chaneil2:k8909@jbchat.abd4i2a.mongodb.net/')  # MongoDB 서버 주소와 포트 설정
db = client['chat']  # 데이터베이스 선택
collection = db['content']  # 컬렉션 선택

# CSV 파일 읽기
data = pd.read_csv('case2_content.csv')
url = data.iloc[0,0]
# 데이터 변환 및 MongoDB에 삽입
document = {
    "_id": url,
    #"url": data.iloc[0, 0],
    "content": data.iloc[2, 0]
}

#collection.delete_many({})  # 데이터 초기화
collection.insert_one(document)  # MongoDB에 데이터 삽입

# 연결 종료
client.close()
