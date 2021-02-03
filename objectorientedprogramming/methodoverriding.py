class parent:
    def mobile(self):
        print("nokia 5310")
class child(parent):
    def mobile(self):
        print("iphone11")
c=child()
c.mobile()
print(c)