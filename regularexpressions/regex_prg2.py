from re import*
pattern='[ab]'#either a or b
pattern="[a-z]"
pattern='[a-zA-Z0-9]'
pattern='[^a-zA-Z0-9]'
matcher=finditer(pattern,"abc _72K@")
for match in matcher:
    print(match.start())#0 1
    print(match.group())#a b
#predefined characters
pattern="\s"
pattern="\d"
pattern="\D"
pattern="\w"
pattern="\W"
matcher=finditer(pattern,"abc _72K@")
for match in matcher:
    print(match.start())#0 1
    print(match.group())#a b
