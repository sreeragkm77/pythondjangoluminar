from datetime import datetime
class bank:
    def create_account(self,acno,pname,balance,bank_name):
        self.acno=acno
        self.pname=pname
        self.balance=balance
        self.bank_name=bank_name
    def deposit(self,amount):
        self.balance+=amount
        print("your account",self.acno,"has been creadited with",amount,"on",datetime.today(),"av balance",self.balance)
    def withdrawal(self,amount):
        if self.balance>amount:
            self.balance-=amount
            print("your account", self.acno, "has been debited with", amount, "on", datetime.today(), "av balance",
                  self.balance)
        else:
            print("transaction canceled error code")
    def balance_enq(self):
        print(self.balance)
obj=bank()
obj.create_account(1000,"ajay",3000,"sbi")
obj.deposit(10000)
