from market import app
from flask import render_template
from market.models import Item

@app.route("/")
@app.route("/home")     # displaye the home page in both cases: http://127.0.0.1:5000/home - http://127.0.0.1:5000
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()    # info. from database.
    return render_template('market.html', items=items)