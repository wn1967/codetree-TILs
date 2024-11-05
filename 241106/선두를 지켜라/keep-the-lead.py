N,M = map(int, input().split())
blank = [0] * 1000001
blank2 = [0] * 1000001
timeline = []

start = 0
time = -1
for i in range(N):
    v,t = map(int, input().split())
    for j in range(t):
        time += 1
        start += v
        blank[time] = start
        timeline.append(time)

start = 0
time = -1
for i in range(M):
    v,t = map(int, input().split())
    for j in range(t):
        time += 1
        start += v
        blank2[time] = start

result = 0
top = 0
count = 0
side  = []
for z in range(len(timeline)):
    if blank[z] > blank2[z]:
        side.append(0)
    elif blank[z] < blank2[z]:
        side.append(1)
    else:
        pass
    
for i in range(len(side)):
    if side[i] != side[i-1]:
        result += 1

print(result)