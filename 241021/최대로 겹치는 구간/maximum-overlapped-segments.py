n = int(input())
array = [0]*300
for i in range(n):
    x,y = map(int, input().split())
    x += 100
    y += 100
    for j in range(x,y+1):
        array[j] += 1

print(max(array))