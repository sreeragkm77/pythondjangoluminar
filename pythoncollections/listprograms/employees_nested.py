employees=[
    [10,"christy","dataanalyst",50000],
    [11,"jhon","ba",30000],
    [12,"sab","dataanalyst",40000],
    [13,"tom","developer",40000],
    [14,"jhoni","developer",30000],
    [15,"sabir","dataanalyst",50000],
    [16,"tino","developer",40000],
    [17,"tomis","developer",47000],
    [18,"jhonis","developer",32000],

]
#print number of employees in this company
number_of_employees=len(employees)
print("number of employees",number_of_employees)
#print total amount of salary
total=0
for emp in employees:
    total+=emp[3]
print("total amount",total)
#group by designation
d_cnt,da_cnt,ba_cnt=0,0,0
for emp in employees:
    if emp[2]=="dataanalyst":
        da_cnt+=1
    elif emp[2]=="developer":
        d_cnt+=1
    else:
        ba_cnt+=1
print("developer =",d_cnt)
print("dataanalyst =",da_cnt)
print("ba =",ba_cnt)
#print highest salaryed employee
salary_list=[]
for emp in employees:
    salary_list.append(emp[3])
print(salary_list)
hig_salary=max(salary_list)
print(hig_salary)
for emp in employees:
    if emp[3]==hig_salary:
        print(emp)
#print lowest salary man as developer
d_salary_list=[]
for emp in employees:
    if(emp[2]=="developer"):
        d_salary_list.append(emp[3])
low_salary=min(d_salary_list)
for emp in employees:
    if (emp[3]==low_salary):
        print(emp)