import datetime

class Creditcard:
  cvv:str
  expiry_year:str
  expiry_mont:str
  expiry_date:datetime
  number:int
  zip_code:int  

  def __init__(self,cvv:str,expiry_year:str,expiry_mont:str,expiry_date:datetime,number:int,zip_code:int) -> None:
    self.cvv = cvv
    self.expiry_year = expiry_year
    self.expiry_mont = expiry_mont
    self.expiry_date = expiry_date
    self.number = number
    self.zip_code = zip_code