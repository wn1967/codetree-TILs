N = int(input())
array = [[0]*201 for _ in range(201)]


for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1+100,x2+100):
        for k in range(y1+100,y2+100):
            array[j][k] = 1
count = 0
for z in range(201):
    for x in range(201):
        count += array[z][x]

print(count)