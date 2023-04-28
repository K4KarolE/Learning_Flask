from market import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=16), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    def __repr__(self):
        return self.username

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=30), nullable=False, unique=True)      # length = name char. limitation
    seen =  db.Column(db.Integer(), nullable=False)
    year = db.Column(db.String(length=9), nullable=False)
    genre = db.Column(db.String(length=30), nullable=False) 
    description = db.Column(db.String(length=200), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item: {self.title}'
    
'''    
terminal: py / python
>>> from market import db
>>> from market import Item
>>> Item.query.all()  
[Item Home Alone, Item Hofeher]     # instead of: [<Item 1>, <Item 2>]
    '''

'''
>>> item1.owner = User.query.filter_by(username='Ted').first().id
>>> db.session.add(item1)
>>> db.session.commit()
>>> i = Item.query.filter_by(title='Home Alone').first()
>>> i.owned_user
User: Ted
'''