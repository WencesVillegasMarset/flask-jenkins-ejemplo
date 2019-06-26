#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)
bd = {
    1:'Juan',
    2:'Mikael',
    3:'Roberto',
    4:'Jose',
    5:'Carlos',
}
@app.route('/')
@app.route('/hello')  # this route is not working
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    # show the user profile for that user
    return 'Hola  %s!\n' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0')  # open for everyone
