class Profile:
  def __init__(self, firstName, lastName, email, sex, profilePicture, tiktok):
    self._firstName: str = firstName
    self._lastName: str = lastName
    self._email: str = email
    self._sex: str = sex
    self._profilePicture: str = profilePicture
    self._tiktok: str = tiktok

  @property
  def firstName(self): return self._firstName
  @property
  def lastName(self): return self._lastName
  @property
  def email(self): return self._email
  @property
  def sex(self): return self._sex
  @property
  def profilePicture(self): return self._profilePicture
  @property
  def tiktok(self): return self._tiktok

  @firstName.setter
  def firstName(self, firstName): self._firstName = firstName
  @lastName.setter
  def lastName(self, lastName): self._lastName = lastName
  @email.setter
  def email(self, email): self._email = email
  @sex.setter
  def sex(self, sex): self._sex = sex
  @profilePicture.setter
  def profilePicture(self, profilePicture): self._profilePicture = profilePicture
  @tiktok.setter
  def tiktok(self, tiktok): self._tiktok = tiktok
