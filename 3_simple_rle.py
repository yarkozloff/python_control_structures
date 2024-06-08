#str = str('aaabbbbccccc')
str = str(input())
lst = []
for symbols in str:
    lst.append(symbols)
lst2 = []
for i in set(lst):
    count = lst.count(i) 
    if count > 1:
        lst2.append(f"{count}{i}")
    else:
        lst2.append(i)
result = ''.join(lst2)
print(result)
