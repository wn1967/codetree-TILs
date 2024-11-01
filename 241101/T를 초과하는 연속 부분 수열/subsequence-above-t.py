n, t = map(int, input().split())

arr = list(map(int, input().split()))

maxv=0
count=1
for i in range(n):
    if arr[i]>3 and arr[i] > arr[i-1]:
        count += 1
        maxv = max(maxv,count)
    else:
        count = 0
        maxv = max(maxv,count)
    
print(maxv)