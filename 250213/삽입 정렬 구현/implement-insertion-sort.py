T = int(input())

arr = list(map(int, input().split()))
leng = len(arr)

for i in range(1,leng):
    j = i-1
    key = arr[i]

    while j >= 0 and arr[j] > key:
        arr[j+1]=arr[j]
        j -=1

    arr[j+1] = key
        
for k in arr:
    print(k, end=' ')
