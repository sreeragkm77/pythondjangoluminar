class Bank:
    def bal_enq(self):
        print("inside balance eq")
    def withdraw(self):
        print("inside withdraw")
    def __deposit(self):
        print("inside deposit")
class Atm(Bank):
    pass
obj=Atm()
obj.bal_enq()
obj.__deposit