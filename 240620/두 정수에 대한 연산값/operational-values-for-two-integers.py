a, b = map(int, input().split())

def check(a,b):
    global aa, bb
    if a > b :
        aa = a + 25
        bb = b* 2
    
    elif a<b :
        aa = a*2
        bb = b+25

    return aa,bb

check(a,b)

print(aa,bb)