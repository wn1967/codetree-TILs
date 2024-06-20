N =int(input())

arr = list(map(int , input().split()))

def aasd(arr):
    for i in range(len(arr)) :
        if arr[i]%2 ==0 :
            arr[i]=arr[i]/2
        print(int(arr[i]), end=' ')

aasd(arr)