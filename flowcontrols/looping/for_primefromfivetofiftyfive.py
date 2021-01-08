low=int(input("enter lower limit"))
upper=int(input("enter upper"))
for num in range(low,(upper+1)):
    flg=0
    for i in range(2,num):
        if (num % i == 0):
            flg = flg + 1
            break
        else:
            flg = 0
    if flg == 0:
        print(num)
