N = int(input())
blank = [0]*31
key = 10
before = 10

for i in range(N):
    A, B = input().split()
    A = int(A)
    if B == "R":
        beforekey = key
        key += A
        for j in range(beforekey+10,key+10):
            blank[j] += 1
        # before -= A

    elif B == "L":
        beforekey = key
        key -= A
        for j in range(key+10,beforekey+10):
            blank[j] += 1
        # before += A

count = 0

for z in range(len(blank)):
    if blank[z] >= 2:
        count += 1

print(count)