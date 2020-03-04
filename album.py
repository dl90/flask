
class Album: # Don
    def __init__(self, title, artist, release_date, art, song_list):
        self.__art:str = art
        self.__title:str = title
        self.__artist:Artist = artist
        self.__release_date:date = release_date
        self.__song_list:List[Song] = song_list

    @property
    def art(self):
        return self.__art
    @art.setter
    def art(self, input):
        if(not input):
            self.__art = input

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, input):
        if(len(input.strip()) > 0):
            self.__title = input

    @property
    def artist(self):
        return self.__artist
    @artist.setter
    def artist(self, input):
        if(len(input.strip()) > 0):
            self.__artist = input

    @property
    def release_date(self):
        return self.__release_date
    @release_date.setter
    def release_date(self, input):
        if(len(input.strip()) > 0):
            self.__release_date = input

    @property
    def song_list(self):
        return self.__song_list
    
    # input type [songs]
    def new_song_list(self, input):
        if(len(input) > 0):
            self.__song_list = input

    # insert song at specific position
    def single_append_song_list(self, input, index=len(self.__song_list) - 1):
        if((type(input) == Song) and (index > 0 and index < len(self.__song_list))):
            self.__song_list.insert(index - 1, input)

