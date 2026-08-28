## OOP Project - Sample Banking Syatem ##
class BankAccount:
    def __init__(self,Acc_Hol_Name, Acc_Number,Balance):
        self.Acc_Hol_Name = Acc_Hol_Name
        self.__Acc_Number = Acc_Number
        self._Balance =Balance
    def CusDetails(self):
        print("Name:",self.Acc_Hol_Name)
        print("ACC_NO:",self.__Acc_Number)
        print("Balance:",self._Balance)
    def Deposite(self,amount):
        if amount>0:  self._Balance += amount
        else:
         print("Invalide Amount")
    def Check_Balance(self):
        print(self._Balance)
# Savings and current Account
class SavingsAccount(BankAccount):
    def Withdraw(self,amount):
         if amount >0 and self._Balance>= amount: self._Balance -= amount
         else:
          print("Enter Valide Amount")

class CurrentAccount(BankAccount):
    overdraft = 5000
    def Withdraw(self,amount):
      if  amount>0 and self._Balance + self.overdraft >=amount:self._Balance -= amount
      else:
         print("Enter a valid amount")
cus_1=SavingsAccount( "Hari",16112002,10000)
cus_2=CurrentAccount("Hari2",22092000,15000)
cus_1.CusDetails()
cus_2.CusDetails()    
## lets do Deposite and withdraw
cus_1.Deposite(5000)
cus_1.Check_Balance()
cus_2.Withdraw(16000)
cus_2.Check_Balance()


