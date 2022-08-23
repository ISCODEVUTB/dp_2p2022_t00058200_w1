from .customer import Customer
from .location import Location
from .enums import PersontypeEnun
from .packageabstract import Package
class Standarpackage(Package):
  id:str
  national_id:str
  id_type:str
  person_type:PersontypeEnun
  name:str
  email:str
  last_name:str
  location:Location
  invoice:str
  credit_car:str
  overweight:float

  def __init__(self, id, code, description, grams_price, base_price, weight, customer,credit_car,overweight) -> None:
    super().__init__(id, code, description, grams_price, base_price, weight, customer)
    self.credit_car= credit_car
    self.overweight = overweight

  def calculate(self) -> float:
    return super().calculate()+self.base_price


