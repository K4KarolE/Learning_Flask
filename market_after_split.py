# after reorg. the market_original.py into market_after_split.py / models.py / routes.py
# copied to __init__.py - market_after_split,py no longer in use

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   # Flask instance
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)    # SQLAlinstance -> future classes into database tables


