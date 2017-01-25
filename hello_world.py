from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

### Youtube tutorial- connecting python with Mongodb w/ mLab and pymongo
app.config['MONGOA_DBNAME'] = 'pythontest'
app.config['MONGO_URI'] = 'mongodb://python:python@ds129469.mlab.com:29469/pythontest'

mongo = PyMongo(app)

@app.route('/add')
def add():
    user = mongo.db.users
    user.insert({'name' : 'Chris'})
    return 'Added User!'

### From thinful curriculum
@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def say_person(name):
    return "Hello {}!".format(name.title())

@app.route("/hellos/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

### running on localhost:8080 instead of cloud9
if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)
