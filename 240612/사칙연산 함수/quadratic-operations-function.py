a,o,c = input().split()
result = 0

ab = int(a)
cb = int(c)

if  o == '+':
    result == ab + cb
elif  o == '-':
    result = ab - cb
elif  o == '*':
    result = ab * cb
elif  o == '/':
    result = ab // cb


print(a,o,c, '=', result)