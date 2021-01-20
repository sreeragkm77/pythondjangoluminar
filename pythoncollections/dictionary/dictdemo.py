expenses={"jan":30000,"feb":25000,"march":28000,"april":25000}
print(expenses["march"])
print("june" in expenses)
expenses["june"]=25000
print(expenses)
expenses["march"]-=3000
print(expenses)
print(expenses["march"])