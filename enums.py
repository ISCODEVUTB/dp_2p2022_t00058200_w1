from enum import Enum

class PersontypeEnun(Enum):
  NATURAL  = 1
  LEGAL    = 2

class Invoicestatus(Enum):
  PROCESSING = 'PROCESSING'
  SENT  = 'SENT'
  REJECTED = 'REJECTED'
  CANCELED = 'CANCELED'
  
class Paymentsmethods(Enum):
  CREDIT= 'CREDIT' 
  DEBIT= 'DEBIT' 
  THRANSFER= 'THRANSFER'
  CASH= 'CASH' 

class OrderStatus(Enum):
  PENDIN = 'PENDIN'
  PAYMENT_DUE_DATE = 'PAYMENT_DUE_DATE'