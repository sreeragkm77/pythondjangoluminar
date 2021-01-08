n=int(input("enter number"))
rev=0
while(n>0):
    temp=n%10
    rev=rev*10+temp
    n=n//10
print("revers of number:",rev)