class employee:
    def set_employee(self,id,ename,desig,salary):
        self.id=id
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def get_employee(self):
        print(self.id,",",self.ename,",",self.desig,",",self.salary)
obj=employee()
obj.set_employee(1000,"ajay","developer",25000)
obj.get_employee()