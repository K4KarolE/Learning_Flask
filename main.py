from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")     # displaye the home page in both cases: http://127.0.0.1:5000/home - http://127.0.0.1:5000
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = [
        {'title': 'Aliens', 'year': 1989, 'genre':'horror', 'seen':6},
        {'title': 'Terminator 2', 'year': 1992, 'genre':'action', 'seen':3},
        {'title': 'Matrix', 'year': 1999, 'genre':'sci-fi', 'seen':12} 

    ]
    return render_template('market.html', items=items)





# @app.route("/")
# def hello_world():
#     return "<h1>Hello, World!</h1> \n <a href='http://127.0.0.1:5000/about'>About</a>"


# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>About page of {username}</h1>'

# @app.route('/about')
# def about_page():
#     return '<h1>Learning Flask</h1>'
