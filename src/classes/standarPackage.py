from .abstracts.Package import Package
class StandarPackage(Package):
  price = 35.2
  def calculate(self) -> float:
    temp =  super().calculate()
    return self.price + temp
    