from market import app
app.app_context().push()
from market.models import User

users = User.query.all()
print('\n')
for i in users:
    print(i)
print('\n')