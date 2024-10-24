n,k,T = input().split()

n = int(n)
k = int(k)

blank = []

for i in range(n):
    word = input()
    if word.startswith(T):
        blank.append(word)

blank2 = sorted(blank)

print(blank2[k-1])