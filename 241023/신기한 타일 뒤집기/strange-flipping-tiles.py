N = int(input())
blank = [0]*2000001
key = 1000000

for i in range(N):
    A, B = input().split()
    A = int(A)
    if B == "R":
        beforekey = key
        key += A
        for j in range(beforekey,key):
            if 0 <= j < 2000001:
                blank[j] = 1

    elif B == "L":
        beforekey = key
        key -= A
        for j in range(key, beforekey):
            if 0 <= j < 2000001:
                blank[j] = 2

wcount = 0
bcount = 0

for z in range(len(blank)):
    if blank[z] == 1:
        bcount += 1
    elif blank[z] == 2:
        wcount += 1
print(wcount, bcount)