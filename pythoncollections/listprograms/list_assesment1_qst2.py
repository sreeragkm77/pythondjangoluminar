lst=[1,2,3,4,5]
num=int(input("enter a number"))
lst1=list()
for i in lst:
    for j in lst:
        if(num==i+j):
            print(i,j)