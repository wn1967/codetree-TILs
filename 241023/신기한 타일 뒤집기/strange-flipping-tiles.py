N = int(input())
blank = [0]*200000
key = 100000

for i in range(N):
    A, B = input().split()
    A = int(A)
    if B == "R":
        beforekey = key
        key += A
        for j in range(beforekey+10000,key+10000):
            blank[j] = 1

    elif B == "L":
        beforekey = key
        key -= A
        for j in range(key+10000, beforekey+10000):
            blank[j] = 2

# print(blank)

wcount = 0
bcount = 0

for z in range(len(blank)):
    if blank[z] == 1:
        bcount += 1
    elif blank[z] == 2:
        wcount += 1
print(wcount, bcount)