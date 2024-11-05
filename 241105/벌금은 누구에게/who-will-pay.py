N,M,K = map(int, input().split())
blank = []
blank2 = [0] * (N+1)
for i in range(M):
    num = int(input())
    blank.append(num)

result = -1

for j in blank:
    blank2[j] += 1
    if blank2[j] >= K:
        result = j
        break

print(result)