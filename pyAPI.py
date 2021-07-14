
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

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/avengers/all', methods=['GET'])
def avengers_all():
    return jsonify(avengers)

@app.route('/avengers', methods=['GET'])
def avengers_properties():
    results = []
    nationality = ""
    if 'nationality' in request.args:
        nationality = request.args['nationality']
    else:
        print("no hero")    

    for avenger in avengers:
        if avenger['nationality'] == nationality:
            results.append(avenger)


    return jsonify(results)

if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost', port=5000)
