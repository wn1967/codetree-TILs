n = int(input())

def check(n):
    if n <= 2:
        return n
    elif 2< n  and n%2 == 1:
        return n+check(n-2)
    elif 2< n  and n%2 == 0:
        return n+check(n-2)

result =  check(n)

print(result)