f=open("mailid","r")
for lines in f:
    line=lines.rstrip("\n")
    from re import *
    rule="[a-zA-Z.]*[0-9]*@+[a-zA-Z.]*"
    matcher=fullmatch(rule,line)
    if matcher==None:
        print("invalid")
    else:
        print("valid===>",line)
