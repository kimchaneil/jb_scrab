import pandas as pd
from pymongo import MongoClient

# MongoDB 연결 설정
client = MongoClient('mongodb+srv://chaneil2:k8909@jbchat.abd4i2a.mongodb.net/')  # MongoDB 서버 주소와 포트 설정
db = client['chat']  # 데이터베이스 선택
collection = db['content']  # 컬렉션 선택


collection.delete_many({})  # 데이터 초기화

# 연결 종료
client.close()
