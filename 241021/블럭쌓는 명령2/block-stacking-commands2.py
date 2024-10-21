N,K = map(int, input().split())
array = [0]*N
for i in range(K):
    A,B = map(int, input().split())
    # if A < 0 or B >= N or A > B:
    #     print("Invalid input: A and B must be within the range of 0 to N-1.")
    #     exit()
    for j in range(A,B+1):
        if j < N:

            array[j] += 1
value = max(array)
print(value)