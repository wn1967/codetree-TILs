N =int(input())

def check(N):
    if N == 0:
        return 

    check(N-1)
    print('HelloWorld')

check(N)