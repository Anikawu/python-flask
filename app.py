
from os import name
from flask import Flask #載入flask
from flask import request #載入request物件
from flask import redirect #載入redirect函式
from flask import render_template
import json
#建立application 物件,可以設定靜態檔案的路徑
app = Flask(
    __name__,
    static_folder="public",#靜態檔案的資料夾名稱
    static_url_path="/www" #靜態檔案對應的網址路徑
    )
#所有在public 資料夾底下的檔案,都對應到網址路徑/www/檔案名稱

#建立路徑/getSum 對應的處理函式
#利用要求字串(Query String)提供彈性:/getSum?min=最小數字&max=最大的數字

@app.route("/getSum")
def getSum(): #1+2+3+...+max
    maxNumber=request.args.get("max",100)#預設值給100
    maxNumber=int(maxNumber)
    minNumber=request.args.get("min",1) #預設值給1
    minNumber=int(minNumber)
    print("最小數字",minNumber)
    print("最大數字",maxNumber)
    result =0
    for n in range(minNumber,maxNumber+1):
        result+=n
    return "結果:"+str(result)

#建立路徑/en/ 對應的處理函式
@app.route("/en/")
def index_english():
    return json.dumps({    #字典轉換成json格式的字串再送到前端 
            "state":"ok",
            "text":"hello flask"
        })

#建立路徑/zh/ 對應的處理函式
@app.route("/zh/")
def index_chinese():
    # return json.dumps({
    #         "state":"ok",
    #         "text":"您好 歡迎光臨"
    #     },ensure_ascii=False) #指示不要用ASCII編碼處理中文 

    return render_template("index",name = "小花")  #呼叫樣板檔案
#建立路徑/ 對應的處理函式
@app.route("/")
def index(): #用來回應路徑/ 對應的處理函式
    #return redirect("https://www.google.com/")  #導向到網址
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
        return redirect("/en/")   #導向到路徑
       
    else: 
        return redirect("/zh/")
       
    

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