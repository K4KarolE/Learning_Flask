from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1> \n <a href='http://127.0.0.1:5000/about'>About</a>"


# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>About page of {username}</h1>'

@app.route('/about')
def about_page():
    return '<h1>Learning Flask</h1>'
