from market import db       # __init__
from market import bcrypt    # __init__
from market import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=16), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            if len(str(self.budget)) >= 7:
                return f'{str(self.budget)[:-6]},{str(self.budget)[-6:-3]},{str(self.budget)[-3:]}$'
            else:
                return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)   # True / False
    
    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price
    
    def can_return(self, item_obj):
        return item_obj in self.items
    

    # def __repr__(self):
    #     return self.username


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=30), nullable=False, unique=True)      # length = name char. limitation
    seen =  db.Column(db.Integer(), nullable=False)
    year = db.Column(db.String(length=9), nullable=False)
    genre = db.Column(db.String(length=30), nullable=False) 
    description = db.Column(db.String(length=200), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    price =  db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'Item: {self.title}, Price: {self.price}'
    
    def buy(self, user):
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()
    
    def return_item(self, user):
        self.owner = None
        user.budget += self.price - 5
        db.session.commit()