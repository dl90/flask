from schema import db
from schema import (User, Profile, Playlist, Artist, Album, Song)

users = User.query.all()
profiles = Profile.query.all()
playlists = Playlist.query.all()

print(users)
print(profiles)
print(playlists)
print('---------------------------------\n')

artists = Artist.query.all()
albums = Album.query.all()
songs = Song.query.all()

print(artists)
print(albums)
print(songs)
print('---------------------------------\n\n')

user = User.query.filter_by(username='test420').first()
print(user.profile)
print('---------------------------------\n')
print(user.playlists)
print('---------------------------------\n\n')

artist = Artist.query.filter_by(first_name='snoop').first()
print(artist.albums)
print('---------------------------------\n')
print(artist.songs)
print('---------------------------------\n')