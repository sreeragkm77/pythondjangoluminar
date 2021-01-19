lst=[1,2,3,4,5]
num=int(input("enter a number"))
lst1=list()
for i in lst:
    for j in lst:
        if(num==i+j):
            print(i,j)
print("-------------")
num=int(input("enter number to pair"))
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]+lst[j]==num):
            print(lst[i],lst[j])
