from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Maria",
        "lastname": "Luna",
        "socialMedia":
        {
            "facebookUser": "marialuna",
            "instagramUser": "marialuna",
            "xUser": "marialuna",
            "linkedin": "maria-luna",
            "githubUser": "marialuna"
        },
        "blog": "https://marialuna.com",
        "author": "Maria Luna"
    }

    return jsonify(value)

if __name__ == '__main__':
    app.run(port=5000)