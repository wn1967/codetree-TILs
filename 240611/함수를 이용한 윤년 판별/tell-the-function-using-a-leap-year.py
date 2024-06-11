n = int(input())

def quar(n):
    result = 'false'
    if n % 4 == 0:
        result = 'true'

    if n % 100 == 0 and n % 400 != 0 :
        result = 'false'

    print(result)    

quar(n)