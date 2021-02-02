class student:
    def set_Student(self,rol,course,name):
        self.rol=rol
        self.course=course
        self.name=name

    def get_student(self):
        print(self.rol,",",self.course,",",self.name)
obj=student()
obj.set_Student(20,"django","ajay")
obj.get_student()
print(obj.course)
print(obj.rol)
#constructor
#__init__()