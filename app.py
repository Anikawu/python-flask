
from flask import Flask #載入flask
from flask import request #載入request物件
#建立application 物件,可以設定靜態檔案的路徑
app = Flask(
    __name__,
    static_folder="public",#靜態檔案的資料夾名稱
    static_url_path="/www" #靜態檔案對應的網址路徑
    )
#所有在public 資料夾底下的檔案,都對應到網址路徑/www/檔案名稱




#建立路徑/ 對應的處理函式
@app.route("/")
def index(): #用來回應路徑/ 對應的處理函式
    #print("請求方法", request.method)
    #print("通訊協定", request.scheme)
    #print("主機名稱", request.host)
    #print("路徑", request.path)
    #print("完整的網址", request.url)
    #print("瀏覽器和作業系統", request.headers.get("user-agent"))
    #print("語言偏好",request.headers.get("accept-language"))
    #print("引薦網址",request.headers.get("referrer"))
    lang=request.headers.get("accept-language")
    print("語言偏好設定",lang)
    if lang.startswith("en"):  #偏好英文設定
        return"hello flask"
    else: 
        return "您好 歡迎光臨"

    return "Hello flask" #回傳網站首頁的內容

#建立路徑/data 對應的處理函式
@app.route("/data")
def handleData():
    return "my data"


#動態路由:建立路徑/ User/使用著名稱 對應的處理函式
@app.route("/user/<username>")
def handleUser(username):
    if username == "語喬":
        return "你好  "+ username
    else:
        return "hello  " +username

#啟動網站伺服器,可透過port參數指定埠號
app.run(port=3000)