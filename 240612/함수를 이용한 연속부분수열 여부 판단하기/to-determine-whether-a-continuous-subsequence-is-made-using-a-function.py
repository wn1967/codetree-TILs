n1, n2 = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(len(A)):
    result = 0
    if A[i] == B[0]:
        for j in range(len(B)):
            if A[i+j] == B[j]:
                result += 1
        if result == len(B):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
        break