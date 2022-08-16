from datetime import date
class CreditCard:
  
  expiry_date:date
  expiry_mont:str
  expiry_year:str
  cvs:int
  number:str
  zip_code:str

  def __init__(self,expiry_date,expiry_mont,expiry_year,cvs,number,zip_code) -> None:
    self.expiry_date  = expiry_date
    self.expiry_mont  = expiry_mont
    self.expiry_year  = expiry_year
    self.cvs  = cvs
    self.number  = number
    self.zip_code  = zip_code


  def validate(self):
    if (
      self.expiry_date and self.cvs and self.number and self.zip_code and self.expiry_mont and self.expiry_year
    ):
      return True
    return False;
