N  = int(input())

def check(N):
    if N== 0 :
        return
    print(N, end=' ')
    check(N-1)
    print(N, end=' ')

check(N)