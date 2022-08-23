from abc import ABC,abstractmethod
from .customer import Customer

"""
  clase abtracta de paquete 
"""
class Package(ABC):
  id:str
  code:str
  description:str
  grams_price:float
  base_price:float
  weight:float
  customer:Customer

  def __init__(self,id,code,description,grams_price,base_price,weight,customer) -> None:
    self.id = id
    self.code = code
    self.description = description
    self.grams_price = grams_price
    self.base_price = base_price
    self.weight = weight
    self.customer = customer

  @property
  def id(self)->str:
    return self.id;  
  @property  
  def code(self)->str:
    return self.code;  
  @property  
  def description(self)->str:
    return self.description;
  @property  
  def grams_price(self)->float:
    return self.grams_price;
  @property  
  def base_price(self)->float:
    return self.base_price;
  @property  
  def weight(self)->float:
    return self.weight;    
  @property  
  def customer(self)->str:
    return self.customer;   

  @property.setter
  def id(self,id)->None:
    self.id = id

  @property.setter
  def code(self,code)->None:
    self.code = code

  @property.setter
  def description(self,description)->None:
    self.description = description

  @property.setter
  def grams_price(self,grams_price)->None:
    self.grams_price = grams_price

  @property.setter
  def base_price(self,base_price)->None:
    self.base_price = base_price

  @property.setter
  def weight(self,weight)->None:
    self.weight = weight

  @property.setter
  def customer(self,customer)->None:
    self.customer = customer

  def calculate (self)->float:
    return  self.base_price*(self.grams_price*self.weight)