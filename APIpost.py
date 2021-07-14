
from flask import Flask
from flask import jsonify, request



app = Flask(__name__)

ironman = {
    "id":1,
    "name":"Tony",
    "nickname":"iron man",
    "nationality":"American",
    "gender":"M",
    "superpower":"n"
}

spiderman = {
    "id":2,
    "name":"Peter",
    "nickname":"spider man",
    "nationality":"American",
    "gender":"M",
    "superpower":"y"
}

blockwidor = {
    "id":3,
    "name":"Natasha",
    "nickname":"Block Widow",
    "nationality":"Russia",
    "gender":"F",
    "superpower":"n"
}

avengers =[ironman, spiderman, blockwidor]


@app.route('/avengers', methods=['POST'])
def avengers_post():
    if 'id' in request.args:
        id = request.args['id']
        print ("id",id)
    if 'name' in request.args:
        name = request.args['name']
        print ("name",name)
    if 'nationality' in request.args:
        nationality = request.args['nationality']
        print ("nationality",nationality)
    if 'nickname' in request.args:
        nickname = request.args['nickname']
        print ("nickname",nickname)
    if 'superpower' in request.args:
        superpower = request.args['superpower']
        print ("superpower",superpower)
    return jsonify(avengers)


if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost', port=3000)
