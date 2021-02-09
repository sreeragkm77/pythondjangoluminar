#map
lst=[1,2,3,4,6]
numlist=list(map(lambda num:num-1 if num<5 else num+1 if num>5 else num,lst))
print(numlist)

names=["india","pak","aus","eng","srilanka"]
upplist=list(map(lambda name:name.upper(),names))
print(upplist)
acountry=list(filter(lambda name:name[0]=='a',names))
print(acountry)
