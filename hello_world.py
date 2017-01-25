from flask import Flask
from os import environ
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGOA_DBNAME'] = 'pythontest'
app.config['MONGO_URI'] = 'mongodb://python:python@ds129469.mlab.com:29469/pythontest'

mongo = PyMongo(app)

@app.route('/add')
def add():
    user = mongo.db.users
    user.insert({'name' : 'Carlo'})
    return 'Added User!'

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def say_person(name):
    return "Hello {}!".format(name.title())

@app.route("/hello/<names>")
def hello_person(names):
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

@app.route('/users/<username>', methods=['POST'])
def new_user(username):
    return

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host=environ['IP'],
    #         port=int(environ['PORT']))
