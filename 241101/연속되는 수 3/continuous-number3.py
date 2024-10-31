N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

count = 1
max_count = 1

for j in range(1, N):
    if (arr[j] > 0 and arr[j - 1] > 0) or (arr[j] < 0 and arr[j - 1] < 0):
        count += 1
    else:
        count = 1
    max_count = max(max_count, count)

print(max_count)