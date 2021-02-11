#first a-k
#second digit divisible by 3
#followed by any number
from re import*
varname=input("enter variable name")
rule="[a-k][369][a-zA-Z0-9]*"
matcher=fullmatch(rule,varname)
if matcher==None:
    print("invalid variable")
else:
    print("valid variable")