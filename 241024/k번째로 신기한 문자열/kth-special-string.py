n,k,T = input().split()

n = int(n)
k = int(k)

blank = []

for i in range(n):
    word = input()
    key = len(T)
    for j in range(key):
        correct = 0
        if word[j] !=  T[j]:
            correct = 1
    
    if correct == 0:
        blank.append(word)

blank2 = sorted(blank)

print(blank2[k-1])