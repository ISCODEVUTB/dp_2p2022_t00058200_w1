from abc import ABC,abstractmethod
import string

"""
  clase abtracta de paquete 
"""
class Package(ABC):
  id:str
  code:str
  description:str
  grams_price:str
  base_price:str
  weight:float
  customer: