a,b = map(int, input().split())
count = 0

def num():
    global count

    for i in range(a,b+1):
        result = 'True'
        number = i
        for j in range(2, number):
            if number % j == 0 :
                result = 'False'
                pass
        
        if result == 'True' and ((i%10) + (i//10))%2 == 0:
            count += 1
    print(count)


num()