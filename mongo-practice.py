#載入pymongo
from typing import Collection
import pymongo
#連線到mongodb雲端資料庫

client = pymongo.MongoClient("mongodb+srv://yoyo:Aa147@mycluster.iumxk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#把資料放進資料庫
db = client.website #選擇操作test資料庫
collection = db.members #選擇操作users集合
#把資料新增到集合中

collection.insert_one({
    "email":"qq147@gmail.com",
    "password" :"qq123"
})

print("資料新增成功")







