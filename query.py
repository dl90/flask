from db import db
from db import User

x = User.query.all()
print(x)