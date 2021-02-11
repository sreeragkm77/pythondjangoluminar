from re import*
no=input("enter phone number")
rule="(91)?\d{10}"
matcher=fullmatch(rule,no)
if matcher==None:
    print("invalid no")
else:
    print("valid no")