from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '3419281c0437d4e8752a7a27'   # randomly generated >>> import os >>> os.urandom(12).hex()                
# app.app_context().push()
db = SQLAlchemy(app)
# db.create_all()

from market import routes

# with app.app_context():
#     db.create_all()

