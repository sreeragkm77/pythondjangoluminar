#polymorphism
#method overloading
class maths:
    def add(self):
        print("no arg")
    def add(self,num1):
        print("one arg")
    def add(self,num1,num2):
        print("two arg")
m=maths()
m.add(10)