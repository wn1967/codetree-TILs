a,b = map(int, input().split())

num = (10000*b)//(a*a)

if num >= 25:
    print(num)
    print('Obesity')
else:
    print(num)