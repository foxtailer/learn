from datetime import datetime as dt
from time import sleep

class Player:

  __LVL, __HEALTH = 1, 100
  __slots__ = ['__lvl', '__health', '__born']  # Set list of all possible atributes of class

  def __init__(self):
    self.__lvl = Player.__LVL
    self.__health = Player.__HEALTH
    self.__born = dt.now()

  # def lvl(self):
  #   return self.__lvl
  
  # def lvl_up(self, n):
  #   self.__lvl += n

  @property
  def lvl(self):
    return self.__lvl, str(dt.now() - self.__born)
  @lvl.setter
  def lvl(self, n):
    self.__lvl += n

  @classmethod
  def set_cld_field(cls, lvl=1):
    cls.__LVL = Player.__typeTest(lvl)

  @staticmethod
  def __typeTest(value):
    if isinstance(value, int):
      return value
    else:
      raise TypeError("Must be int")


Player.set_cld_field(10)
a = Player()

sleep(1)
a.lvl = 1
print(a.lvl)

#a.key = 1  # raise exeption cose 'key' not in __slots__