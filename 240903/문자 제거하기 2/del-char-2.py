a,n = input().split()
a = list(a)
n = int(n)

for i in range(n):
    number = int(input())

    if 1<= number <= len(a):
        a.pop(number-1)
    else:
        continue

    result = ''.join(a)
    print(result)