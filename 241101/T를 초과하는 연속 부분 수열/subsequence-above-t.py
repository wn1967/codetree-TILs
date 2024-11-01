n, t = map(int, input().split())

arr = list(map(int, input().split()))

maxv=0
count=0

for i in range(n):
    if arr[0] > t:
        count = 1

for i in range(1,n):
    if arr[i]>t and arr[i] > arr[i-1]:
        count += 1
        maxv = max(maxv,count)
    elif arr[i]<t:
        count = 0
        maxv = max(maxv,count)
    elif arr[i]>t and arr[i] <= arr[i-1]:
        count += 1
        maxv = max(maxv,count)
    else:
        count = 0
        maxv = max(maxv,count)

#     print(f'count : {count}')
# print(f'maxv : {maxv}')
print(maxv)