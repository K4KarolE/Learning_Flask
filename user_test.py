from market import app
app.app_context().push()
from market.models import User
from market.models import Item

# users = User.query.all()
# print('\n')
# for i in users:
#     print(i)
# print('\n')

items = Item.query.all()
print('\n')
for i in items:
    print(i)
print('\n')



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