from db import db
from db import User

a = User(username="test", password="awefwef", profileInfo={ "testing":"testing"}, recommendations={ "abc" }, likes={ "efg" }, playHistory={ "hij" }, isPremium=False)
b = User(username="asdf", password="asdfsd")

# https://docs.sqlalchemy.org/en/13/orm/session_api.html
db.session.add_all([a, b])
db.session.commit()