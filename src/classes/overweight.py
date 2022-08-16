from .abstracts.Package import Package
class OverWP(Package):
  price = 12.3
  def calculate(self) -> float:
    temp =  super().calculate()
    if self.weight >=10:
      temp = self.weight*self.price + temp;
    else:
      return temp