from market import app
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash     # error messages

from market.models import Item
from market.models import User

from market.forms import RegisterForm
from market import db   # located in the __init__ file -> not needed: from market.__init__ import db

@app.route("/")
@app.route("/home")     # displaye the home page in both cases: http://127.0.0.1:5000/home - http://127.0.0.1:5000
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()    # info. from database.
    return render_template('market.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: # no validationn errors -> errors dictionary is empty
        for error_message in form.errors.values():
            flash(f'Error occurred: {error_message}', category='danger')
    return render_template('register.html', form=form) 