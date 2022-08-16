import random
from  .abstracts.Package import Package
from .enums.enums import OrderStatus
from customer import Customer
from position import Location

class Order:
  id = random.randint(100000,999999)
  package:Package
  is_paid:bool
  price:float
  receiver:Customer
  sender:Customer
  status:OrderStatus
  location :Location

  def _init_(self, package: Package, is_paid: bool, price: float, receiver: Customer, sender: Customer, status: OrderStatus, location: Location) -> None:
        self.package = package
        self.is_paid = is_paid
        self.price = price
        self.receiver = receiver
        self.sender = sender
        self.status = status
        self.location = location

  def get_package(self) -> Package:
      return self.package

  def set_package(self, package: Package) -> None:
      self.package = package

  def get_paid(self) -> bool:
      return self.is_paid

  def set_is_paid(self, is_paid: bool) -> None:
      self.is_paid = is_paid

  def get_price(self) -> float:
      return self.price

  def set_price(self, price: float) -> None:
      self.price = price

  def get_receiver(self) -> Customer:
      return self.receiver

  def set_receiver(self, receiver: Customer) -> None:
      self.receiver = receiver

  def get_sender(self) -> Customer:
      return self.sender

  def set_status(self, status: OrderStatus) -> None:
      self.status = status

  def get_location(self) -> Location:
      return self.location
  def set_sender(self, sender: Customer) -> None:
      self.sender = sender

  def get_status(self) -> OrderStatus:
      return self.status


