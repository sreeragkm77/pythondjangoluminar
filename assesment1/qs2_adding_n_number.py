num=input("enter number")
i=1
data=0
if(0<int(num)<10):
    while(i<=int(num)):
        res=num*i
        data+=int(res)
        i+=1
    print(data)
else:
    print("enter value less than ten")