f=open("studentname1","r")
h=open("failedstudents.py","r")
student=[]
failed=[]
for line1 in f:
    student.append(line1.rstrip("\n"))
for line2 in h:
    failed.append(line2.rstrip("\n"))
print(student)
print(failed)
sset=set(student)
fset=set(failed)
diff=sset.difference(fset)
print(sset)
print("passed :",diff)