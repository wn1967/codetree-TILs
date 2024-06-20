N = int(input())

arr = list(map(int, input().split()))

def absloute(arr):
    for i in range(N):
        arr[i] = abs(arr[i])
    

absloute(arr)

for j in range(N):
    print(arr[j], end=' ')