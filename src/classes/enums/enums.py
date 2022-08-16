from enum import Enum

class PersonType(Enum):
  NATURAL = 1
  LEGAL = 2
class DocumentType(Enum):
  DNI = 1
  PASSPORT = 2

class Role(Enum):
  ADMIN = 1
  USER = 2
  DRIVER = 3
class OrderStatus(Enum):
  PENDING = 1
  PAYMENT_DUE_DATE = 2
