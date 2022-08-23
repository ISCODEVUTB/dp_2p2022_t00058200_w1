import imp
from re import L
from .person import Person
from .location import Location
from .invoice import Invoice
from .credit_card import Creditcard
class Customer(Person):
  invoices : list[Invoice]
  credit_card :list[Creditcard]
  shipping : list[Location]
  def __init__(self, id, national_id, id_type, person_type, name, email, last_name, location,invoice,credit_car) -> None:
    self.invoices.append(invoice)
    self.credit_card.append(credit_car)
    self.shipping.append(location)
    
    super().__init__(id, national_id, id_type, person_type, name, email, last_name, location)



  def biomatricValidation(self)->bool:
    return True