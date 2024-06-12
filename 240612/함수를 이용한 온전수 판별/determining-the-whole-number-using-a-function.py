a,b = map(int, input().split())
count = 0

def perfect(n):
    global count
    if n%2 != 0 and n%10 != 5:
        if n%3 != 0 or n%9 == 0:
            count += 1

for n in range(a,b+1):
    perfect(n)

print(count)