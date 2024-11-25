import modules.instruments # used in from_obj() classmethod
from modules.instruments import Instrument
from datetime import datetime


class Song():
  max_len_str_attr = 25

  def __init__(self, title :str, artist:str, release_year: int, instrument: Instrument, instrument_brand):
    self.__title = title
    self.__artist = artist
    self.__release_year = release_year
    self.__instrument = instrument
    self.__instrument_brand = instrument_brand

  @classmethod
  def from_obj(cls, obj:dict):
    keys = ['title', 'artist', 'release_year', 'instrument', 'instrument_brand']
    for key in keys:
      if key not in obj:
        raise ValueError(f"Impossible d'instancier une chanson depuis l'objet '{obj}'")
    
      return cls(obj["title"], obj["artist"], obj["release_year"], obj["instrument"], obj["instrument_brand"])
    

  @property
  def title(self) -> str:
     return self.__title
  @title.setter
  def title(self, title:str):
      self.__title = title if 0 <= len(title) <= self.max_len_str_attr else self.__title

  @property
  def artist(self) -> str:
    return self.__artist
  @artist.setter
  def artist(self, artist :str):
      self.__artist = artist if 0 <= len(artist) <= self.max_len_str_attr else self.__artist
    
  @property
  def release_year(self) -> int:
      return self.__release_year
  @release_year.setter
  def release_year(self, release_year :int):
      current_year = datetime.now().year
      self.__release_year = release_year if 0 <= len(release_year) <= self.max_len_str_attr else self.__release_year

  @property
  def instrument(self) -> Instrument:
      return self.__instrument
  @instrument.setter
  def instrument(self, instrument :Instrument):
     self.__instrument = instrument if 0 <= len(instrument) <= self.max_len_str_attr else self.__instrument


  def __str__(self)-> str:
       return (f"Titre: {self.title}\n"
               f" Artiste: {self.artist}\n"
               f" Année de sortie: {self.release_year}\n"
               f" Instrument: {self.instrument}(brand = '{self.__instrument_brand}')")
  def play(self):
      print(f"Joue {self.title:<25} solo avec   ***  {self.instrument:<8}***   du fabricant {self.__instrument_brand:<15}")