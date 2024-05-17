a = int(input())
templist = []
while a > 0:
  templist.append(a % 10)
  a = a // 10
templist = templist[::-1] # Разложили число в list 
print (templist);
total=0
for i in templist:
 total += i # Записываем результат каждого сложения элементов 
print (total);