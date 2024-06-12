a,b = map(int, input().split())

def checkdate(a,b):
    global result
    if a == 2:
        if b in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]:
            result = 'Yes'
            return result
        else:
            result = 'No'

            return result

    elif a in [1,3,5,7,8, 10,12]:
        if b in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]:
            result = 'Yes'

            return result
        else:
            result = 'No'

            return result

    elif a in [4,6,9,11]:
        if b in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]:
            result = 'Yes'

            return result
        else:
            result = 'No'
            return result
    else:
        result = 'No'

checkdate(a,b)

print(result)