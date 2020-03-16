from typing import List
from classes.Profile import Profile
from classes.Song import Song

class User():
  def __init__(self, username, profileInfo, recommendations, likes, playHistory, isPremium=False):
    self._username: str = username
    self._profileInfo: Profile = profileInfo
    self._recommendations: List[Genre] = recommendations
    self._likes: List[Song] = likes
    self._playHistory: List[Song] = playHistory
    self._isPremium: bool = isPremium

  @property
  def username(self): return self._username
  @property
  def profileInfo(self): return self._profileInfo
  @property
  def recommendations(self): return self._recommendations
  @property
  def likes(self): return self._likes
  @property
  def playHistory(self): return self._playHistory
  @property
  def isPremium(self): return self._isPremium

  @username.setter
  def username(self, username): self._username = username
  @profileInfo.setter
  def profileInfo(self, profileInfo): self._profileInfo = profileInfo
  @recommendations.setter
  def recommendations(self, recommendations): self._recommendations = recommendations
  @likes.setter
  def likes(self, likes): self._likes = likes
  @playHistory.setter
  def playHistory(self, playHistory): self._playHistory = playHistory
  @isPremium.setter
  def isPremium(self, isPremium): self._isPremium = isPremium

  def addLike(self, song: Song): self._likes.append( song )
  def addPlayHist(self, song: Song): self._playHistory.append( song )
