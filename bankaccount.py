class BalanceException(Exception):
     pass
class BankAccount:
    def __init__(self,initalAmount,acctName):
         self.balance=initalAmount
         self.name=acctName
         print(f"\nAccount '{self.name}' created. \nBalance ={self.balance:.2f}")
    def getBalance(self):
         print(f"\n Account '{self.name}' balance =${self.balance:.2f}")    
    def deposit(self,amount):
         self.balance=self.balance+amount
         print(f"\nDeposit complete")
         self.getBalance()
    def viableTransaction(self,amount):
          if self.balance>=amount:
               return 
          else:
               raise BalanceException(
                    f"\n Sorry ,account '{self.name}' only has a balance of ${self.balance:.2f}"
               )
    def withdraw(self,amount):
          try:
             self.viableTransaction(amount)
             self.balance=self.balance-amount  
             print('\nWithdraw complete')
          except BalanceException as error:
               print(f'\n Withdraw interrupted:{error}')
    def transfer(self,amount,account):
         try:
              print("\n************\n\n Beginning Transfer..")
              self.viableTransaction(amount)
              self.withdraw(amount)
              account.deposit(amount)
              print(
                   "\n Transfer complete!\n\n****************")
         except BalanceException as error:
              print(f'/n Transfer interrupted:{error}')


class InterestRewardAccount(BankAccount):
     def deposit(self, amount):
          self.balance=self.balance+(amount*1.05)
          print('\nDeposite complete.')
          self.getBalance()

class SavingsAccount(InterestRewardAccount):
     def __init__(self, initalAmount, acctName):
          super().__init__(initalAmount,acctName)
          self.fee = 5
     def withdraw(self,amount):
        try:
          self.viableTransaction(amount+self.fee)
          self.balance=self.balance - (amount+self.fee)
          print("\nWithdraw completed.")
          self.getBalance()
        except  BalanceException as error:
          print(f"\nWithdraw interrupted:{error}")  


Dave =BankAccount(1000,"Dev")
Sara=BankAccount(2000,"Sara")

Dave.getBalance()
Dave.deposit(3000)

Dave.withdraw(3000)
Dave.getBalance()

Dave.transfer(500,Sara)


Jim=InterestRewardAccount(1000,"Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100,Dave)

Rohit=SavingsAccount(2000,"Rohit")
Rohit.getBalance()
Rohit.deposit(100)
Rohit.transfer(100,Dave)
