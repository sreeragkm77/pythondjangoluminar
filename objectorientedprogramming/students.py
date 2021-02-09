class student:
    def __init__(self,rol,name,course,total):
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
obj=student(1000,"akshy","django",140)
obj1=student(1001,"ajay","mean",150)
obj2=student(1002,"tom","django",145)
slist=[]
slist.append(obj)
slist.append(obj1)
slist.append(obj2)
total=0
for stud in slist:
    if stud.course=="django":
        print(stud.name)
        total+=stud.total
        print(total)



