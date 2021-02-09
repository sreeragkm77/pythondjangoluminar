#exception
#error
n1=int(input())
n2=int(input())
#res=n1/n2
#print("res=",res)
#exceptionhandling
#try,except,finally
try:
    res=n1/n2
    print("res=",res)
except Exception as e:
    print("exception occured")
print("i hve one database transaction")
print("i have file operation")