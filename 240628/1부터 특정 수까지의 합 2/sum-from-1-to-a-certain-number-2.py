n = int(input())

def check(n):
    if n == 1:
        print(1)
        return
    
    print(n*(n+1)//2) 

check(n)