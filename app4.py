

from os import name
from flask import Flask #載入flask
from flask import request #載入request物件
from flask import redirect #載入redirect函式
from flask import render_template
from flask import session

#建立application 物件,可以設定靜態檔案的路徑
#http://127.0.0.1:2000/pic1.png
app = Flask(
    __name__,
    static_folder="public",#靜態檔案的資料夾名稱
    static_url_path="/" #靜態檔案對應的網址路徑
    )

app.secret_key="any string but secert"
@app.route("/")
def index():
    return render_template("index.html")

#使用 get 方法處理路徑 /hello
@app.route("/hello")
def hello():
    name=request.args.get("name","")
    session["username"]=name  #session["欄位名稱"]=資料
    return "你好,"+name
#使用 get 方法處理路徑 /talk
@app.route("/talk")
def talk():
    name=session["username"]
    return name+" ,很高興見到你"
     
#啟動網站伺服器,可透過port參數指定埠號
app.run(port=2000)