a,b = map(int, input().split())

count = 0

def isthis():
    global count
    for j in range(a,b+1):
        number = str(j)
        blank=[]

        if j % 3 == 0:
            count += 1
        
        else:
            for k in range(len(number)):
                blank.append(int(number[k]))
                if blank[k] == 3 or blank[k] == 6 or blank[k] == 9 :
                    count += 1

isthis()    

print(count)