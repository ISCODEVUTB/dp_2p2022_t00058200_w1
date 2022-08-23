from .enums import Invoicestatus,Paymentsmethods
from .invoice import Invoice
class Invoice :
  id:str
  status:Invoicestatus
  client:any
  orders:list[Invoice]
  tax:float
  price:float
  discoint:float
  payment_method:Paymentsmethods

  def __init__(self,id:str,status:Invoicestatus,client:str,tax:str,price:str,discoint:str,payment_method:Paymentsmethods) -> None:
    self.id = id 
    self.status = status 
    self.client = client 
    self.tax = tax 

    self.price = price 
    self.discoint = discoint 
    self.payment_method = payment_method 

  # * getters method 
  @property  
  def id(self)->str:
    return self.id

  @property  
  def status(self)->str:
    return self.status

  @property  
  def client(self)->str:
    return self.client

  @property  
  def tax(self)->str:
    return self.tax

  @property  
  def price(self)->str:
    return self.price

  @property  
  def discoint(self)->str:
    return self.discoint

  @property  
  def payment_method(self)->Paymentsmethods:
    return self.payment_method

  # * setters methods
  @id.setter
  def id(self,id)->None:
    self.id = id    

  @status.setter 
  def status(self,status)->None:
    self.status = status    

  @client.setter
  def client(self,client)->None:
    self.client = client

  @tax.setter 
  def tax(self,tax)->None:
    self.tax = tax

  @price.setter 
  def price(self,price)->None:
    self.price = price

  @discoint.setter 
  def discoint(self,discoint)->None:
    self.discoint = discoint

  @payment_method.setter
  def payment_method(self,payment_method)->None:
    self.payment_method = payment_method
      
