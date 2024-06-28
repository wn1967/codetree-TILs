n = int(input())
result = 0

def check(n):
    global result 

    if n == 1:
        print(result)
        return 
    
    if n%2 ==0 :
        n //= 2
        result += 1

    elif n%2 == 1 and n != 1:
        n = n // 3
        result += 1

    check(n)

check(n)