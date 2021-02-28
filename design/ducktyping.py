class swift:
    def drive(self):
        print("driving swift car")
class sonet:
    def drive(self):
        print("driving sonet")
class person:
    def start(self,car):
        car.drive()
sw=swift()
p=person()
p.start(sw)