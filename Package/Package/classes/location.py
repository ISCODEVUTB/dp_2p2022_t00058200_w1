from audioop import add


class Location:
  country:str;
  state:str;
  city:str;
  address_line1:str;
  address_line2:str;
  zip_code:str;


  def __init__(self,country,citi,state,add1,add2,zip_c) -> None:
    self.country = country
    self.state = state
    self.city = citi
    self.address_line1 = add1
    self.address_line2 = add2
    self.zip_code = zip_c
  def getCountry(self):
    return self.country;
  def getstate(self):
    return self.state;
  def getciti(self):
    return self.city;
  def get_add1(self):
    return self.address_line1
  def get_add2(self):
    return self.address_line2;
  
 
