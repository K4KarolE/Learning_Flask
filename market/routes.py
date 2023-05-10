from market import app
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash     # error messages
from flask import request

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user

from market.models import Item
from market.models import User

from market.forms import RegisterForm
from market.forms import LoginForm
from market.forms import PurchaseItemForm
from market.forms import ReturnItemForm


from market import db   # located in the __init__ file -> not needed: from market.__init__ import db

@app.route("/")
@app.route("/home")     # displaye the home page in both cases: http://127.0.0.1:5000/home - http://127.0.0.1:5000
def home_page():
    return render_template('home.html')


@app.route('/market', methods=['GET', 'POST'])
@login_required     # need to loggin before reach market page init / login_manager.login_view = "login_page"
def market_page():
    purchase_form = PurchaseItemForm()
    return_form = ReturnItemForm()
    if request.method == "POST":
        # PURCHASE ITEM
        purchased_item = request.form.get('purchased_item')     #request checking all the forms -> form attribute of request
        purchased_item_object = Item.query.filter_by(title=purchased_item).first()
        if purchased_item_object:
            if current_user.can_purchase(purchased_item_object):
                purchased_item_object.buy(current_user)
                # purchased_item_object.owner = current_user.id     # instead of this 3 lines function created in models Item / buy()
                # current_user.budget -= purchased_item_object.price
                # db.session.commit()
                flash(f"You rented the {purchased_item_object.title} for {purchased_item_object.price}.", category='success')
            else:
                flash(f'Sorry, your budget is not enough to rent {purchased_item_object.title}.', category='danger')
        # RETURN ITEM
        returned_item = request.form.get('returned_item')
        returned_item_object = Item.query.filter_by(title=returned_item).first()
        if returned_item_object:
            if current_user.can_return(returned_item_object):
                returned_item_object.return_item(current_user)
                flash(f"You returned {returned_item_object.title}.", category='success')
            else:
                flash(f"Sorry something went wrong returning {returned_item_object.title}.", category='danger')
        return redirect(url_for('market_page'))

    if request.method == "GET":
        items = Item.query.filter_by(owner=None)    # owner=None -> only not rented yet
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items, return_form=return_form)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)     # models / @password.setter
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully. You are logged in as: {user_to_create.username}', category='success')
        return redirect(url_for('market_page'))
    if form.errors != {}: # no validationn errors -> errors dictionary is empty
        for error_message in form.errors.values():
            flash(f'Error occurred: {error_message}', category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password1.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not matching! Please try again!', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out.", category='info')
    return redirect(url_for("home_page"))