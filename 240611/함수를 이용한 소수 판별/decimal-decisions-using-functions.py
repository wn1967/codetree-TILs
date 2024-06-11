a,b = map(int, input().split())
blank = []

def prime(number):
    result = 'True'

    for j in range(2, number):
        if number % j == 0 :
            result = 'False'            
        
    if result == 'True':
         blank.append(i)

    return

for i in range(a,b+1):
    number = i
    if i ==1 : 
        break
    prime(number)


print(sum(blank))