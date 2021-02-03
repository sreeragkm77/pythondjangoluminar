class parent:
    def m1(self):
        print("inside parent")
class child(parent):
    def m2(self):
        print("inside child")
class subchild(child):
    def m3(self):
        print("inside subchild")
obj=subchild()
obj.m1()
obj.m2()