a = int(input())
while a  > 10:
  templist = []
  while a > 0:
    templist.append(a % 10)
    a //=10
  templist.reverse()
  print(templist)
  a = sum(templist)
  print(a);
  
'''
3456888999
[3, 4, 5, 6, 8, 8, 8, 9, 9, 9]
69
[6, 9]
15
[1, 5]
6
'''

  
