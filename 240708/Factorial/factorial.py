n = int(input())

def fact(n):
    if n <= 1:
        return 1
    else:
        return (n)*fact(n-1)
    
fact(n)
result = fact(n)

print(result)