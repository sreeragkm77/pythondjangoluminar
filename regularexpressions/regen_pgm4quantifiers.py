#quantifiers
from re import *
pattern="a+"
pattern="a*"
pattern="a?"
pattern="a{2,4}"
matcher=finditer(pattern,"aaaaaaaababaabaaa")
for match in matcher:
    print(match.start(),"==>",match.group())