from re import L
from .customer import Customer
from .enums import OrderStatus
from .location import Location
class Order:
  id:str
  paid:bool
  price:float
  receiver:Customer
  sender:Customer
  status:OrderStatus
  location:Location

  def __init__(self,id:str,paid:bool,price:float,receiver:Customer,sender:Customer,status:OrderStatus,location:Location) -> None:
    self.id = id
    self.paid = paid
    self.price = price
    self.receiver = receiver
    self.sender = sender
    self.status = status
    self.location = location

  # * getters methods
  @property
  def id(self)->str:
    return self.id  

  @property
  def paid(self)->bool:
    return self.paid

  @property
  def price(self)->float:
    return self.price

  @property
  def receiver(self)->Customer:
    return self.receiver

  @property
  def sender(self)->Customer:
    return self.sender

  @property
  def status(self)->OrderStatus:
    return self.status

  @property
  def location(self)->str:
    return self.location
  
  # * setter methods 
  
  @id.setter
  def id(self,id)->None:
    self.id = id

  @paid.setter  
  def paid(self,paid)->None:
    self.paid = paid

  @price.setter  
  def price(self,price)->None:
    self.price = price

  @receiver.setter  
  def receiver(self,receiver)->None:
    self.receiver = receiver

  @sender.setter  
  def sender(self,sender)->None:
    self.sender = sender
    
  @status.setter  
  def status(self,status)->None:
    self.status = status

  @location.setter  
  def location(self,location)->None:
    self.location = location