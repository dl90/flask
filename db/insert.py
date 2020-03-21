from schema import db
from schema import (User, Profile, Playlist, Artist, Album, Song)


user1 = User(username="test", password="abc", recommendations={ "abc" }, likes=["song1", "song2"])
user2 = User(username="test420", password="123")
db.session.add_all([user1, user2])
db.session.commit()


profile1 = Profile(1, "abcd@efgh.com", user1, "aaa")
profile2 = Profile(2, "asdf@adsf.com", user2, "bbb")
db.session.add_all([profile1, profile2])
db.session.commit()


playlist1 = Playlist(1, "test's playlist1")
playlist2 = Playlist(1, "test's playlist2")
playlist3 = Playlist(2, "test420's playlist1")
db.session.add_all([playlist1, playlist2, playlist3])
db.session.commit()


artist1 = Artist(first_name="snoop", last_name="dawg", album_list=["hit1", "hit2", "hit3"])
artist2 = Artist(first_name="drake", last_name="bake")
db.session.add_all([artist1, artist2])
db.session.commit()


album1 = Album("hit1", artist1, ["song1", "song2"])
album2 = Album("hit2", artist1, ["song1", "song2"])
album3 = Album("hit3", artist1, ["song1", "song2"])
album4 = Album("hit1", artist2, ["song1", "song2"])
db.session.add_all([album1, album2, album3, album4])
db.session.commit()

song1 = Song("420", artist1, album1, "abcd efg hijk lmn ", rating=10)
song2 = Song("420a", artist1, album1, "abcd efg hijk lmn ", rating=9)
song3 = Song("420b", artist1, album1, "abcd efg hijk lmn ", rating=8)
song4 = Song("420c", artist1, album1, "abcd efg hijk lmn ", rating=7)
song5 = Song("420d", artist1, album1, "abcd efg hijk lmn ", rating=6)
song6 = Song("x", artist2, album4, "abcd efg hijk lmn ", rating=5)
song7 = Song("xx", artist2, album4, "abcd efg hijk lmn ", rating=4)
db.session.add_all([song1, song2, song3, song4, song5, song6, song7])
db.session.commit()