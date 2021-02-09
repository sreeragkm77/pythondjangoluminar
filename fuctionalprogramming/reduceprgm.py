from functools import reduce
lst=[10,11,12,13,14]
sum=reduce(lambda no1,no2:no1+no2,lst)
print(sum)
low=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(low)