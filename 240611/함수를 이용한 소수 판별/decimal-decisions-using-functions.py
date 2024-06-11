a,b = map(int, input().split())
blank = []

def prime(number):
    result = 'True'
    for j in range(2, number):
        if number % j == 0 :
            result = 'False'            
        
    if result == 'True':
         blank.append(i)

for i in range(a,b+1):
    number = i
    prime(number)
    # for j in range(2, number):
    #     if number % j == 0 :
    #         result = 'False'            
        
    # if result == 'True':
    #      blank.append(i)


print(sum(blank))