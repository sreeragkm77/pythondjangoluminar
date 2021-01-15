lst=[10,11,12,13,14,15,16,17]
lst1=list()
lst2=list()
for num1 in lst:
    if(num1%2==0):
        lst1.append(num1)
    else:
        lst2.append(num1)
print(lst1)
print(lst2)
print("evensum",sum(lst1))
print("oddsum",sum(lst2))