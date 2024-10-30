N = int(input())
array = [[0]*201 for _ in range(201)]

for i in range(N):
    x1, y1 = map(int, input().split())

    for j in range(x1, x1+8):
        for k in range(y1, y1+8):
            array[j][k] += 1

count = 0

for z in range(201):
    for x in range(201):
        if array[z][x] >= 1:
            count += 1 

print(count)