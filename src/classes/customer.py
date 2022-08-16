from .enums.enums import DocumentType,PersonType
from .abstracts.Person import Person
from position import Location

class Customer(Person):
  invoices:list[bool]
  shippings:list[Location]

  def __init__(self, id: str, national_id: str, id_type: DocumentType, name: str, last_name: str, person_type: str, email: str) -> None:
    
    super().__init__(id, national_id, id_type, name, last_name, person_type, email)
