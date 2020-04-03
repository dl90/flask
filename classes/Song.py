from typing import List
from datetime import date
from classes.Artist import Artist


class Song:
    def __init__(self, title, artist, realeaseDate, coverArt, lyrics):
        self.__title: str = title
        self.__coverArt: str = coverArt
        self.__artist: Artist = artist
        self.__lyrics: str = lyrics
        self.__realeaseDate: date = realeaseDate

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, input):
        if (len(input.strip()) > 0):
            self.__title = input

    @property
    def coverArt(self):
        return self.__coverArt

    @coverArt.setter
    def coverArt(self, input):
        if (not input):  # if (input) ?
            self.__coverArt = input

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, input):
        if (len(input.strip()) > 0):
            self.__artist = input

    @property
    def lyrics(self):
        return self.__lyrics

    @lyrics.setter
    def lyrics(self, input):
        if (not input):  # if (input) ?
            self.__lyrics = input

    @property
    def release_date(self):
        return self.__release_date

    @release_date.setter
    def release_date(self, input):
        if (len(input.strip()) > 0):
            self.__release_date = input
