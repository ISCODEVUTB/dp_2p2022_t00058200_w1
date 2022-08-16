from abc import ABC, abstractmethod
from customer import Customer
class Package(ABC):
  id:str
  GRAMSPRICE:float = 10
  code:int
  description:str
  weight:float
  customer:Customer

  def __init__(self,code,desc,weight,customer) -> None:
    self.code = code
    self.description = desc
    self.weight = weight
    self.customer = Customer

  def get_id(self) -> str:
    return self.id

  def get_grams_price(self) -> float:
      return self.GRAMSPRICE

  def get_code(self) -> int:
      return self.code

  def set_code(self, code: int) -> None:
      self.code = code
  
  def get_description(self) -> str:
      return self.description

  def set_description(self, description: str) -> None:
      self.description = description

  def get_weight(self) -> float:
      return self.weight

  def set_weight(self, weight: float) -> None:
      self.weight = weight

  def get_customer(self) -> Customer:
      return self.customer

  def set_customer(self, customer: Customer) -> None:
      self.customer = customer

  @abstractmethod
  def calculate(self) -> float:
      return self.weight * self.GRAMSPRICE
