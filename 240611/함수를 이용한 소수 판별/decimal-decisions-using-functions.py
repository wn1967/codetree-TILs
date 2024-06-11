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
    if a==b==1:
        pass
    
    number = i
    prime(number)


print(sum(blank))