import threading
import time
def display():
    for i in range(1,10):
        time.sleep(1)
        print("child thread exicuting")
    print(threading.currentThread().getName())
t=threading.Thread(target=display)
t.start()
for i in range(1,10):
    time.sleep(1)
    print("main thread exicuting")
print(threading.currentThread().getName())
