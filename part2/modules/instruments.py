
from abc import ABC, abstractmethod

INSTRUMENT_NAME_WIDTH = 16

class Instrument(ABC):
  def __init__(self, brand: str):
    self._brand = brand
  
  def __repr__(self) -> str:
      return f"{self.__class__.__name__}(brand = '{self._brand}')"
    
  def __str__(self)-> str:
      return self.__repr__()
    
  @abstractmethod
  def play(self):
      pass


class Guitar(Instrument):
  def __init__(self, brand: str):
    super().__init__(brand)

  def play(self):
    return "*** guitare ***".ljust(INSTRUMENT_NAME_WIDTH) + f"  du fabricant {self._brand}"


class Piano(Instrument):
  def __init__(self, brand: str):
    super().__init__(brand)

  def play(self):
   return "*** piano ***".ljust(INSTRUMENT_NAME_WIDTH) + f"  du fabricant {self._brand}"


class Drum(Instrument):
  def __init__(self, brand:str):
    super().__init__(brand)

  def play(self):
   return "*** batterie ***".ljust(INSTRUMENT_NAME_WIDTH) + f"  du fabricant {self._brand}"