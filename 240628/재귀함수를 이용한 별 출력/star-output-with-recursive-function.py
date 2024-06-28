n =int(input())

def call(n):
    if n ==0 :
        return
    call(n-1)
    print('*'*n)

call(n)