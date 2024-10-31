N = int(input())
blank = []
for i in range(N):
    aa = int(input())
    blank.append(aa)

blank2 = []

cnt = 0
for j in range(N):
    cnt += 1
    if blank[j] == blank[j-1]:
        
        blank2.append(cnt)
    elif blank[j] != blank[j-1]:
        blank2.append(cnt)
        cnt = 1

print(max(blank2))