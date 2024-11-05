N,M = map(int, input().split())
check1 = []
check11 = []
check2 = []
check22 = []

start = 1000
count = 0
for i in range(N):
    d, t = input().split()
    t = int(t)
    for j in range(1,t+1):
        if d == 'R':
            start += 1
            check1.append(start)
            count += 1
            check11.append(count)
        else:
            start -= 1
            check1.append(start)
            count += 1
            check11.append(count)

start = 1000
count = 0

for i in range(M):
    d, t = input().split()
    t = int(t)
    for j in range(1,t+1):
        if d == 'R':
            start += 1
            check2.append(start)
            count += 1
            check22.append(count)
        else:
            start -= 1
            check2.append(start)
            count += 1
            check22.append(count)
result  = 0
answer = 0
for z in range(len(check11)):
    if check1[z] == check2[z]:
        result = 1
        answer = z+1
        break
    else:
        result = -1     

if result == 1:
    print(answer)
else:
    print(-1)