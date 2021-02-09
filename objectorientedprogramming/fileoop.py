class employees:
    def __init__(self,eid,name,desig,exp,salary):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.exp=exp
        self.salary=salary
    def __str__(self):
        return self.name
f=open("employees.py","r")
emplist=[]
salist=[]
for lines in f:
    eid,name,desig,exp,salary=lines.rstrip("\n").split(",")
    emplist.append(employees(eid,name,desig,exp,salary))

for employee in emplist:
    salist.append(employee.salary)
highsal=max(salist)
print(highsal)
for employee in emplist:
    if employee.salary==highsal:
        print(employee)
#low salary earned developer
lowsal=[]
for employee in emplist:
    if employee.desig=="developer":
        lowsal.append(employee.salary)
lowsalary=min(lowsal)
print(lowsalary)
for employee in emplist:
    if (employee.desig=="developer")&(employee.salary==lowsalary):
        print(employee)
dev_sal_list=[]
for employee in emplist:
    if employee.desig=="developer":
        dev_sal_list.append(employee.salary)
    print(dev_sal_list)
high=list(reduce(lambda no1,no2))







