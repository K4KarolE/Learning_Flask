from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   # Flask instance
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)    # SQLAlinstance -> future classes into database tables

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=30), nullable=False, unique=True)      # length = name char. limitation
    seen =  db.Column(db.Integer(), nullable=False)
    year = db.Column(db.String(length=9), nullable=False)
    genre = db.Column(db.String(length=30), nullable=False) 
    description = db.Column(db.String(length=200), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.title}'
    '''
    terminal: py / python
    >>> from market import db
    >>> from market import Item
    >>> Item.query.all()  
    [Item Home Alone, Item Hofeher]     # instead of: [<Item 1>, <Item 2>]
    '''

@app.route("/")
@app.route("/home")     # displaye the home page in both cases: http://127.0.0.1:5000/home - http://127.0.0.1:5000
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()    # info. from database
    
    # first/dummy information
    # items = [
    #     {'title': 'Aliens', 'year': 1989, 'genre':'horror', 'seen':6},
    #     {'title': 'Terminator 2', 'year': 1992, 'genre':'action', 'seen':3},
    #     {'title': 'Matrix', 'year': 1999, 'genre':'sci-fi', 'seen':12} 

    return render_template('market.html', items=items)
