class BankA:
  name_bank:str
  id_bank :str;
  id_account:str;

  def __init__(self,acc_id,name,bnk_id) -> None:
    self.id_account = acc_id;
    self.id_bank = bnk_id;
    self.name_bank = name;
  # methos 

  def get_name(self):
    return self.name_bank;

  def get_id_bank(self):
    return self.id_bank;
  
  def get_id_acc(self):
    return self.id_account;
  
  def set_name(self,name):
     self.name_bank = name;
  
  def set_id_bank(self,id_b):
    self.id_bank = id_b;
  
  def set_id_acc(self,id_a):
    self.id_account = id_a;

  def toString(self):
    return 'bank name {} bank id {} account id {}'.format(self.name_bank,self.id_bank,self.id_account)
  
