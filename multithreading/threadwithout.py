from threading import*
class Myclass:
    def job(self):
        for i in range(10):
            print("child class")
obj=Myclass()
t=Thread(target=obj.job)
t.start()
for i in range(10):
    print("main thread class")