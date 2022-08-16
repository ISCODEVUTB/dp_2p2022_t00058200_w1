class BankAccount :
  account_id:str
  bank_name:str
  bank_id:str
  amount:float  = 0.0
  
  def __init__(self,account_id:str,bank_name:str,bank_id:str) -> None:
    self.account_id = account_id
    self.bank_name = bank_name
    self.bank_id = bank_id;

  def deposit(self,amount:float)->bool:
    self.amount = self.amount + amount;
    return True;