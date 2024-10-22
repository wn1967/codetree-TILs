N = int(input())
blank = [0]*10000
key = 10
before = 10

for i in range(N):
    A, B = input().split()
    A = int(A)
    if B == "R":
        beforekey = key
        key += A
        for j in range(beforekey+5000,key+5000):
            blank[j] += 1

    elif B == "L":
        beforekey = key
        key -= A
        for j in range(key+5000,beforekey+5000):
            blank[j] += 1

count = 0

for z in range(len(blank)):
    if blank[z] >= 2:
        count += 1

print(count)