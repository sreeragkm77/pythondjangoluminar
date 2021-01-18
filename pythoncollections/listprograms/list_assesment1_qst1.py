lst=[3,4,5]
lst1=list()
num0=lst[1]+lst[2]
num1=lst[0]+lst[2]
num2=lst[0]+lst[1]
lst1.append(num0)
lst1.append(num1)
lst1.append(num2)
print(lst1)
#or
print("-----------")
out=list()
total=sum(lst)
for num in lst:
    out.append(total-num)
print(out)