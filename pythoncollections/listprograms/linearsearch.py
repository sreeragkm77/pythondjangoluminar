limit=int(input("enter limit"))
lst=list()
for i in range(0,limit):
    number=input("enter number")
    lst.append(number)
element=int(input("enter element you want to search"))
flag=0
cnt=0
for number in lst:
    if(element==number):
        flag+=1
        break
    else:
        pass
    cnt+=1
if flag==0:
    print("element not found")
else:
    print("element found at",cnt)