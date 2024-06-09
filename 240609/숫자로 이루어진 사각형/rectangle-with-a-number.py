n= int(input())

def squa():
    cnt = 1
    for a in range(n):
        for b in range(n):
            print(cnt, end=' ')
            cnt += 1
            if cnt == 10:
                cnt = 1
        print()

squa()