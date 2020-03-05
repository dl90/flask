import album

class Artist:
  def __init__(self, firstName, lastName, album_list, album_art):
    self.__firstName:str = firstName #
    self.__lastName:str = lastName
    self.__album_list:List[Album] = []
    self.__album_art:str = album_art


  @property
  def firstName(self):
      return self.__firstName

  @firstName.setter
  def art(self, input):
      if(not input):
          self.__art = input


  @property
  def lastName(self):
      return self.__lastName

  @lastName.setter
  def lastName(self, input):
      if(not input):
          self.__art = input


  @property
  def album_list(self):
      return self.__album_list


  @property
  def album_art(self):
    return self.__album_art

  @album_art.setter
  def album_art(self, input):
      if(not input):
          self.__album_art = input



  def add_album(self, album): self.__album_list.append(album)

  #deletes album
  def delete_album(self, album): self.__album_list.remove(album)


  #deletes all albums 
  def wipe_discography(self): self.__album_list.clear()
