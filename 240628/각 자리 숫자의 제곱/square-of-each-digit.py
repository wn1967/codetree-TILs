n = int(input())
result = 0

def check(n):
    global result
    if n == 0 :
        return
    
    result += (n%10)*(n%10)

    check(n//10)

check(n)
print(result)