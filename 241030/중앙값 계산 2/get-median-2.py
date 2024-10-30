N = int(input())
array = list(map(int, input().split()))
blank = []
blank2 = []
for i in range(N):
    blank.append(array[i])
    blank.sort()
    if (i+1)%2 == 1:
        blank2.append(blank[len(blank)//2])

for j in range(len(blank2)):
    print(blank2[j], end=' ')