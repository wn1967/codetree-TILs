a,b = map(int, input().split())
def change(a,b):
    a,b = b,a
    return a,b

a,b = change(a,b)

print(a,b)