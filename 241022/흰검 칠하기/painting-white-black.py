N = int(input())
blank = [1]*10000
blank2= [1]*10000
blank3= [1]*10000
key = 5000

for i in range(N):
    A, B = input().split()
    A = int(A)
    if B == "R":
        beforekey = key
        key += A
        for j in range(beforekey+100,key+100):
            blank[j] = 2
            blank2[j] += 1

    elif B == "L":
        beforekey = key
        key -= A
        for j in range(key+100,beforekey+100):
            blank[j] = 3
            blank3[j] += 1

for g in range(len(blank)):
    if blank2[g] >=3 and blank3[g]>=3:
        blank[g] = 0

wcount = 0
bcount = 0
gcount = 0

for z in range(len(blank)):
    if blank[z] == 3:
        wcount += 1
    elif blank[z] == 2:
        bcount += 1
    elif blank[z] == 0:
        gcount += 1

print(wcount, bcount, gcount)