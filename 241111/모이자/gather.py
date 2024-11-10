n = int(input())

arr = list(map(int, input().split()))
blank=[]
for i in range(n):
    goal = arr[i]
    count = 0
    for j in range(n):
        count += abs(i - j) * arr[j]
    blank.append(count)
print(min(blank))