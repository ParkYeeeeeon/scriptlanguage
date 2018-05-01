class BankAccount:
    def __init__(self,balance,name,number):
        self.balance=balance
        self.name=name
        self.number=number
    def withdraw(self,amount) :
        self.balance-=amount
    def deposit(self,amount):
        self.balance+=amount
    def __str__(self):
        return "계좌번호:"+self.number+"\n잔액"+str(self.balance)+"\n이름:"+str(self.name)

class SavingAccount(BankAccount):
    def __init__(self,balance,name,number,interest_rate):
        super().__init__(balance,name,number)
        self.interest_rate=interest_rate
    def add_interest(self):
        self.balance+=self.balance*self.interest_rate
    def __str__(self):
        return super().__str__()+"\n이자율:"+str(self.interest_rate)
s=SavingAccount(1000000,"박연","2016184016",0.03)

class CheckingAccounts(BankAccount):
    def __init__(self,balance,name,number,withdraw_charge):
        super().__init__(balance,name,number)
        self.withdraw_charge=withdraw_charge
    def withdraw(self,amount):
        super().withdraw(amount+self.withdraw_charge)
    def __str__(self):
        return super().__str__()+"출금 수수료:"+str(self.withdraw_charge)

print(s)
s.add_interest
c=CheckingAccounts(1000000,"kim","7777-1111",500)
print(c)

