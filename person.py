from abc import ABC,abstractmethod
from .enums import Persontype
from .location import Location

# * abstract class Person for Customer and Internal
class Person:
  id:str
  national_id:str
  id_type:str
  person_type:Persontype
  name:str
  email:str
  last_name:str
  location:Location

  def __init__(self,id,national_id,id_type,person_type,name,email,last_name,location) -> None:
    self.id = id
    self.national_id = national_id
    self.id_type = id_type
    self.person_type = person_type
    self.name = name
    self.email = email
    self.last_name = last_name
    self.location = location

  # * getters methods
  @property
  def id(self)->str:
    return self.id

  @property
  def national_id(self)->str:
    return self.national_id

  @property
  def person_type(self)->Persontype:
    return self.person_type
  
  @property
  def name(self)->str:
    return self.name

  @property
  def email(self)->str:
    return self.email

  @property
  def last_name(self)->str:
    return self.last_name
  
  @property
  def location(self)->Location:
    return self.location
  
   # * setters methods 
  @id.setter
  def id(self,id:str)->None:
    self.id = id;

  @national_id.setter
  def national_id(self,national_id:str)->None:
    self.national_id = national_id

  @person_type.setter
  def person_type(self,person_type)->None :
    self.person_type = person_type
  
  @name.setter
  def name(self,name:str)->None:
    self.name = name

  @email.setter
  def email(self,email)->None:
    self.email = email

  @last_name.setter 
  def last_name(self,last_name)->None:
    self.last_name = last_name
  
  @location.setter
  def location(self,location:Location)->None:
    self.location = location
