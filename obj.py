from typing import List
from datetime import date
import datetime


# firstname, lastname, title, artist, album, date, art, time, song, lyrics, 

class Artist: #jaime
  def __init__(self, firstName, lastName, album_list, artist_dp):
    # self._firstName:str = firstName
    # self._lastName:str = lastName
    # self._albums:List[Album] = []
    # self._photo:str = artist_dp

    self._firstName = firstName
    self._lastName = lastName
    self._albums = []
    self._photo = artist_dp

  def add_album(self, album): self._albums.append(album)
  def change_photo(self, photo): self._photo = photo

class Album: # Don
    def __init__(self, title, artist, release_date, art, song_list):
        self.__art:str = art
        self.__title:str = title
        self.__artist:Artist = artist
        self.__release_date:date = release_date
        self.__song_list:List[Song] = song_list

    def get_art(self):
        return self.__art
    def get_title(self):
        return self.__title
    def get_artist(self):
        return self.__artist
    def get_release_date(self):
        return self.__release_date
    def get_song_list(self):
        return self.__song_list

# def make_album(art, title, artist, release_date, song_list):
#   	state = False
#     if typeof(art) == 
#   	Album(art, title, artist, release_date, song_list)

class Song: #jaime
    def __init__(self, title, artist, realeaseDate, lyrics):
        self._title:str = title
        self._artist:Artist = artist
        self._lyrics:str = lyrics
        self._realeaseDate:date = realeaseDate


test_artist = Artist("Chris", "Ng", [], "github.com")

x = datetime.datetime.now()

test_song1 = Song("R", test_artist, x, "abcdefg")
test_song2 = Song("Ru", test_artist, x, "abcdefg")
test_song3 = Song("Rus", test_artist, x, "abcdefg")
test_song4 = Song("Rusty", test_artist, x, "abcdefg")
test_song5 = Song("Rusto", test_artist, x, "abcdefg")
test_song6 = Song("Rusti", test_artist, x, "abcdefg")

_list = [test_song1, test_song2, test_song3, test_song4, test_song5, test_song6]
test_album = Album( "rusty musty", test_artist, x, "github.com/chris", _list)

test_artist.add_album(test_album)
print(test_artist._albums[0].get_title())


# class User:
#     def __init__(self, name, profileInfo, preferences, likes, playHistory, accountType = False):
#         self.name = name
#         self.profileInfo:Profile = profileInfo
#         self.accountType:bool = accountType
#         self.preferences:List[Song] = preferences 
#         self.likes:List[Song] = likes
#         self.playHistory:List[Song] = playHistory

class User: #refactor profile_info to class
    def __init__(self, name, profileInfo, preferences, likes, playHistory, accountType = False):
        self.name = name
        self.profileInfo:dict = profileInfo
        self.accountType:bool = accountType
        self.preferences:List[Song] = preferences 
        self.likes:List[Song] = likes
        self.playHistory:List[Song] = playHistory # TODO creation date, last played date

jaime = { #refactor to class
    'email': 'jaime@jaime.com',
    'name': "chris",
    'preferred_name': 'jaime',
    'gender': 'fluid',
    'profile_picture': "github/jaime",
    'facebook': 'facebook.com/jaime',
    'gitlab': 'gitlab.com/jaime',
    'tiktok': 'tiktok.com/jaime',
    'snapchat': 'snap.com/jaime',
    'myspace': "myspace.com/chris"
}

chrisN = User("ChrisN", jaime, [test_song1, test_song2], [test_song1, test_song2], [test_song1, test_song2], True)

class Playlist: # Don
    def __init__(self, name, songs, date, numberOfSongs, genreOfSongs):
        self.__name = name
        self.__songs = songs
        self.__date = date
        self.__numberOfSongs = len(self.__songs)
        self.__genreOfSongs = genreOfSongs
