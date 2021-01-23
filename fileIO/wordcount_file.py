f=open("data","r")
dict={}
for line in f:
    word=line.rstrip("\n").split(" ")
for wrd in word:
    if wrd not in dict:
        dict[wrd]=1
    else:
        dict[wrd]+=1
for k,v in dict.items():
    print(k,v)