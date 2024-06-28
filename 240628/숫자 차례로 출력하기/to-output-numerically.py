n =int(input())

def call(n):
    if n == 0 :
        return
    call(n-1)
    print(n, end=' ')

def back(n):
    if n == 0 :
        return
    print(n, end=' ')
    back(n-1)

call(n)
print()
back(n)