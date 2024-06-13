Y,M,D = map(int, input().split())
Spring = [3,4,5]
Summer = [6,7,8]
Fall = [9,10,11]
Winter = [12,0,1,2]

def isthis(Y,M,D):
    global prime
    prime = True
    if Y%4==0:
        prime = False

        if Y%100 == 0 :
            prime = True

            if Y%400 == 0 :
                prime = False

    else:
        prime = True

    return prime

isthis(Y,M,D)

def ok(Y,M,D):
    global real 
    real = True

    # 윤년 아닐때
    if prime == True:
        if M in [4,6,9,11]:
            if D ==31 :
                real = False
                return real
        elif M==2:
            if D in [29,30,31] :
                real = False
                return real

    # 윤년일때
    else:
        if M in [4,6,9,11]:
            if D ==31 :
                real = False
                return real
            else:
                real = True
                return True
        elif M==2:
            if D in [30,31] :
                real = False
                return real
            else:
                real = True
                return True

ok(Y,M,D)

if real == False:
    print(-1)
else:
    if M in Spring:
        print('Spring')
    elif M in Summer:
        print('Summer')
    elif M in Fall:
        print('Fall')
    elif M in Winter:
        print('Winter')
    else:
        print(-1)