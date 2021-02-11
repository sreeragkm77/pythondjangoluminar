f=open("phonenumbers","r")
validno=[]
for lines in f:
    line=lines.rstrip("\n")

    from re import*
    rule="(91)?\d{10}"
    matcher=fullmatch(rule,line)
    if matcher==None:
        print("invalid")
    else:
        print("valid===>",line)
        validno.append(line)
        print(validno)
    rule1="[a-zA-Z]{2}\d{2}[a-zA-Z]{2}\d{4}"
    matcher1=fullmatch(rule1,line)
    if matcher1==None:
        print("invalid")
    else:
        print("valid==>",line)
