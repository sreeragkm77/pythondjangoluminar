regno=input("enter vehicle regno")
from re import*
rule="kl[0-9][0-9][a-zA-Z][a-zA-Z][0-9][0-9][0-9][0-9]"
rule1="kl\d{2}[a-zA-Z]{2}\d{4}"
matcher=fullmatch(rule1,regno)
if matcher==None:
    print("invalid reg no")
else:
    print("valid reg no")