class Location:
  country:str
  state:str
  city:str
  address_line_1:str
  address_line_2:str
  zip_code:str

  def __init__(self,country,state,city,address_line_1,address_line_2,zip_code) -> None:
    self.country = country
    self.state = state
    self.city = city
    self.address_line_1 = address_line_1
    self.address_line_2 = address_line_2
    self.zip_code = zip_code

    