n = int(input())
offset = 100
border = 201
blank = [[0] * 201 for _ in range(border)]

for i in range(n):
    x1,y1,x2,y2 = map(int, input().split())

    if i%2 == 0 :
        for a in range(x1+offset,x2+offset):
            for b in range(y1+offset,y2+offset):
                blank[a][b] = 1
    elif i%2 == 1 :
        for a in range(x1+offset,x2+offset):
            for b in range(y1+offset,y2+offset):
                blank[a][b] = 2

count = 0
for j in range(border):
    for k in range(border):
        if blank[j][k] == 2:
            count += 1

print(count)