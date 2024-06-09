n = int(input())

def check(a):
    global result
    result = a%10 + a//10
check(n)

if n%2 == 0 and result%5==0:
    print('Yes')
else:
    print('No')