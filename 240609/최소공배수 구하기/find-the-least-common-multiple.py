a,b = map(int, input().split())
result = 0
def xas(n,m):
    global result
    abc = 500

    for i in range(max(n,m), n*m+1):
        if i%n == 0 and i%m ==0 and i < abc:
            abc=i
            result = abc
        
xas(a,b)

print(result)