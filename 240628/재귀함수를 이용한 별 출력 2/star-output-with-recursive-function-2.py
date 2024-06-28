n = int(input())

def callback(n):
    if n==0 :
        return

    
    print("* " * n , end=' ')
    print()

    callback(n-1)

    print("* " * n , end=' ')
    print()

callback(n)