array = [[0]*2001 for _ in range(2001)]
OFFSET = 1000

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


for z in range(x1+OFFSET,x2+OFFSET):
    for x in range(y1+OFFSET,y2+OFFSET):
        array[z][x] += 1
    
for z in range(x3+OFFSET,x4+OFFSET):
    for x in range(y3+OFFSET,y4+OFFSET):
        array[z][x] = 0


blank = []
for a in range(2001):
    count = 0
    for b in range(2001):
        if array[a][b] >= 1:
            count += 1
    blank.append(count)

blank2 = []

for c in range(2001):
    count2 = 0
    for d in range(2001):
        if array[d][c] >= 1:
            count2 += 1
    blank2.append(count2)

print(max(blank)*max(blank2))