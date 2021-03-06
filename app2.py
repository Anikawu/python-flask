

from flask import Flask #載入flask
from flask import request #載入request物件
from flask import redirect #載入redirect函式
from flask import render_template

#建立application 物件,可以設定靜態檔案的路徑
#http://127.0.0.1:2000/pic1.png
app2 = Flask(
    __name__,
    static_folder="public",#靜態檔案的資料夾名稱
    static_url_path="/" #靜態檔案對應的網址路徑
    )

@app2.route("/")
def index():
    return render_template("index.html")

#處理路徑/page 的對應函式
@app2.route("/page")
def page():
    return render_template("page.html")


#啟動網站伺服器,可透過port參數指定埠號
app2.run(port=2000)