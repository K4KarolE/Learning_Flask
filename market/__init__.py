from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '3419281c0437d4e8752a7a27'   # randomly generated >>> import os >>> os.urandom(12).hex()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)    # OOP - getters and setters
from market import routes

# with app.app_context():
#     db.create_all()

