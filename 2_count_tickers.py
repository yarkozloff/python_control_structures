a = int(input())
rows = [[0,1,1,0,0],[1,0,0,0,1],[0,0,0,0,0]]
#a = 3

mainrow = []
for i in range(len(rows)):
    row = rows[i]
    count = 0
    for j in range(len(row)):
        if row[j] == 0 and count < a:
            count += 1
            if count == a: 
                mainrow.append(i)   
                #print(mainrow)
        else:
            count = 0
if len(mainrow) != 0:
    print("Свободный ряд",mainrow[0])
else:
    print("Нет свободных рядов")
    

