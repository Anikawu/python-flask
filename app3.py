

from flask import Flask #載入flask
from flask import request #載入request物件
from flask import redirect #載入redirect函式
from flask import render_template

#建立application 物件,可以設定靜態檔案的路徑
#http://127.0.0.1:2000/pic1.png
app = Flask(
    __name__,
    static_folder="public",#靜態檔案的資料夾名稱
    static_url_path="/" #靜態檔案對應的網址路徑
    )
#使用get方法,處理路徑/的對應函式
@app.route("/")
def index():
    return render_template("index.html")

#處理路徑/page 的對應函式
@app.route("/page")
def page():
    return render_template("page.html")

#處理路徑/show 的對應函式
@app.route("/show")
def show():
    name= request.args.get("n","")
    return "welcome, "+name

#處理路徑/calculate 的對應函式
@app.route("/calculate",methods=["POST"])
def calculate():
    #接收GET方法的QUERY STRING
    #maxNumber= request.args.get("max","")
    #接收 POST 方法的QUERY STRING
    maxNumber=request.form["max"]
    maxNumber=int(maxNumber)
    result=0
    for n in range(1,maxNumber+1):
        result+=n
    return render_template("result.html",data=result)

#啟動網站伺服器,可透過port參數指定埠號
app.run(port=5000)