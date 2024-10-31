N = int(input())
blank = []
for i in range(N):
    aa = int(input())
    blank.append(aa)

cnt = 0
for j in range(N):
    if blank[j] == 0 or blank[j] != blank[j-1]:
        cnt += 1

print(cnt)