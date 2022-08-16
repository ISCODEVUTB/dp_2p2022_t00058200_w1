class Position:
  lat:float
  lng:float

  def __init__(self,lat:float,lng:float) -> None:
    self.lat = lat
    self.lng = lng

  # getter methods of properties
  def get_lat(self)->str:
    return self.lat

  def get_lng(self)->str:
    return self.lng

  # setter methods of properties 
  def set_lat(self,lat:float)->None:
    self.lat = lat;
  
  def set_lng(self,lng:float)->None:
    self.lng = lng;
class Location:
  """
    public attributes of class Location
  """
  country:str
  state:str
  city:str
  address_line1:str
  address_line2:str
  zip_code:str
  
  def __init__(self,country:str,state:str,
                city:str,address_line1:str,address_line2:str,zip_code:str) -> None:
    
    self.address_line1 = address_line1;
    self.address_line2 = address_line2;
    self.zip_code = zip_code;
    self.city = city;
    self.country = country;
    self.state = state;
  
  