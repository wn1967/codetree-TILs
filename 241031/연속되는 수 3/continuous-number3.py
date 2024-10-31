N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

# print(arr)
arr2 = []
count = 1
for j in range(1,N):
    if arr[j] > 0 and arr[j-1] >0:
        count += 1
    elif arr[j] > 0 and arr[j-1] < 0:
        count = 1
    elif arr[j] < 0 and arr[j-1] >0:
        count = 1
    elif arr[j] < 0 and arr[j-1] < 0:
        count += 1

    arr2.append(count)
    # print(count)
print(max(arr2))