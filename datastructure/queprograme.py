size=int(input("enter size of que"))
n=1
rear=0
front=0
que=[]
def insertion():
    item=int(input("enter item"))
    global rear
    if rear>=size:
        print("que full")
        print(rear)
    else:
        que.insert(rear,item)
        rear+=1
def deletion():
    global front
    if front<rear:
        print(que[front],"deleted")
        front+=1
    elif front==rear:
        print("que empty")
def display():
    for i in range(0,size):
        print(que[i])
while(n!=0):
    option=int(input("enter option 1)insertion 2)deletion 3)display"))
    if option==1:
        insertion()
    elif option==2:
        deletion()
    elif option==3:
        display()
n=int(input("do you want to continue press 0 to exit"))