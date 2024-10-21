n = int(input())
array = [0]*101
for i in range(n):
    x,y = map(int, input().split())
    for j in range(x,y+1):
        array[j] += 1

print(max(array))