from market import db

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
