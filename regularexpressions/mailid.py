from re import*
mail=input("enter mail id")
rule='[a-zA-Z.]*[0-9]*@gmail.com'
matcher=fullmatch(rule,mail)
if matcher==None:
    print("invalid")
else:
    print("valid")