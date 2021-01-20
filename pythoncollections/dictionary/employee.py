employe={"id":100,"ename":"ajay","exp":2,"salary":35000}
if("salary" in employe):
    print(employe["salary"])
if("gender" in employe):
    print("exceist")
else:
    employe["gender"]="male"
print(employe)
if(employe["salary"]<=35000):
    employe["salary"]+=5000
print(employe)    