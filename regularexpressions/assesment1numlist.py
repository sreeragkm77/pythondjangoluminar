lst1=[1,2,5,6,7,8]
lst2=[2,5,3,9,6,4]

final=list(filter(lambda x:x in lst1,lst2))
print(final)
#