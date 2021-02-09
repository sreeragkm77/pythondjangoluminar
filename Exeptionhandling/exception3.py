n1=int(input("n1"))
n2=int(input("n2"))
try:
    res=n1/n2
    print("res=",res)
except:
    n2 = int(input("n2"))
    res = n1 / n2
    print("res=", res)
finally:
    print("i have database")