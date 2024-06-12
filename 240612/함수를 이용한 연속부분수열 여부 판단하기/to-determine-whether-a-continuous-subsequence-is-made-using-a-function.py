n1, n2 = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0

def check():
    global result
    for i in range(n1):
        result = 0
        if A[i] == B[0]:
            for j in range(n2):
                if i + j >= n1 or A[i+j] != B[j]:
                    break
                result += 1
            if result == n2:
                return

check()

if result == n2:
    print('Yes')
else:
    print('No')