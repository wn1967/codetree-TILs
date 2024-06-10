def isthis(a,b):
    count = 0


    for j in range(a,b+1):
        number = str(j)
        blank=[]

        if j % 3 == 0:
            count += 1
        
        else:
            if '3' in number or '6' in number or '9' in number:
                count += 1
    return count

a,b = map(int, input().split())


result = isthis(a,b)    

print(result)