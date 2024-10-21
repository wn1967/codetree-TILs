N,K = map(int, input().split())
array = [0]*N
for i in range(K):
    A,B = map(int, input().split())
    for j in range(A,B+1):
        array[j] += 1

print(max(array))