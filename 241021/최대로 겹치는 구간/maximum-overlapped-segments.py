n = int(input())
array = [0]*201
for i in range(n):
    x,y = map(int, input().split())
    x += 100
    y += 100
    for j in range(x,y):
        array[j] += 1
print(max(array))