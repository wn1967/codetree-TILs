N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

maxvalue = 0
count = 1
for j in range(N):
    
    if arr[j] > arr[j-1]:
        count += 1
        maxvalue = max(count, maxvalue)
    else:
        count = 1
        maxvalue = max(count, maxvalue)
    
print(maxvalue)