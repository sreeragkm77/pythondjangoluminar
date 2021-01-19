lst=[1,2,3,5]
low=0
upp=len(lst)-1
ele=int(input("enter element"))
while(low<=upp):
    tot=lst[low]+lst[upp]
    if(ele==tot):
        print(lst[low],lst[upp])
        break
    elif(ele>tot):
        low+=1
    elif(ele<tot):
        upp-=1