import datetime
import Song


class Playlist:  # Don
    def __init__(self, name, songs, date, numberOfSongs, genreOfSongs):
        self.__name = name
        self.__songs = songs    # array of songs
        self.__date = date      # datetime
        self.__num_of_songs = len(self.__songs)
        self.__genre = genreOfSongs

        # self.__name:str = name
        # self.__songs:song.Song = songs            # array of songs
        # self.__date:datetime.datetime = date      # datetime
        # self.__num_of_songs:int = len(self.__songs)
        # self.__genre:str = genreOfSongs

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, input):
        if(len(input.strip()) > 0):
            self.__name = input

    @property
    def songs(self):
        return self.__songs

    # insert song at specific position
    def single_song_append_playlist(self, input):
        index = self.__numberOfSongs - 1
        if((type(input) == song.Song) and (index > 0 and index < len(self.__songs))):
            self.__song_list.insert(index - 1, input)

    # merge two playlists
    def merge_playlist(self, input):
        if(type(input) == list and len(input) > 0):
            self.__songs.extend(input)

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, input):
        if(type(input) == datetime.datetime):
            self.__date = input

    @property
    def num_of_songs(self):
        return self.__num_of_songs

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genere(self, input):
        if(len(input.strip()) > 0):
            self.__genre = input
