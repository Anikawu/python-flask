#載入pymongo
from typing import Collection
import pymongo
#連線到mongodb雲端資料庫

client = pymongo.MongoClient("mongodb+srv://yoyo:Aa147@mycluster.iumxk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#把資料放進資料庫
db = client.website #選擇操作test資料庫
collection = db.users #選擇操作users集合
#把資料新增到集合中
#取得集合中第一筆資料
#data=collection.find_one()
#print(data)
#根據objectId取得文件資料
#data = collection.find_one(objectId("60ed098ce1eaf50e444dd691"))
#print(data)
#print(data["_id"])
#print(data["email"])


#一次取得多筆文件資料
cursor =collection.find()
print(cursor)

#使用for迴圈逐一取得資料
for doc in cursor:
    print(doc["name"])  #只針對有興趣的欄位印出來








