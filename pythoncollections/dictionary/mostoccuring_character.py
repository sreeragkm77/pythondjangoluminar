pattern="ABABBACEEEEEEEEE"
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
for key,value in dict.items():
    print(key,",",value)
print(dict)
print(dict.get("E"))
data=sorted(dict,key=dict.get,reverse=True)
print(data)