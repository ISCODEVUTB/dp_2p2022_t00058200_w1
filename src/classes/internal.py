from .abstracts.Person import Person
from .enums.enums import DocumentType,Role
from .bank_account import BankAccount
class Internal (Person):
  role:Role
  account:BankAccount

  def __init__(self, id: str, national_id: str, id_type: DocumentType,
    name: str, last_name: str, person_type: str, email: str,role:Role,account:BankAccount) -> None:
    # llamamos al conructor de la clase que estamos heredando
    super().__init__(id, national_id, id_type, name, last_name, person_type, email)
    self.role = role
    self.account = BankAccount

  def get_role(self)->Role:
    return self.role
     
