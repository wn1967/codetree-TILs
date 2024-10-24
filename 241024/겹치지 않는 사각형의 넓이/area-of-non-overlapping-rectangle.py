array = [[0]*2001 for _ in range(2001)]


x1, y1, x2, y2 = map(int, input().split())
for j in range(x1+1000,x2+1000):
    for k in range(y1+1000,y2+1000):
        array[j][k] = 1

x3, y3, x4, y4 = map(int, input().split())
for q in range(x3+1000,x4+1000):
    for w in range(y3+1000,y4+1000):
        array[q][w] = 2    

x5, y5, x6, y6 = map(int, input().split())
for e in range(x5+1000,x6+1000):
    for r in range(y5+1000,y6+1000):
        array[e][r] = 0

count = 0

for z in range(2001):
    for x in range(2001):
        if array[z][x] == 1:
            count += 1
        elif array[z][x] == 2:
            count += 1 

print(count)