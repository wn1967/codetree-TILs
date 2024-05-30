text = input()
n = int(input())

for i in range(n):
    print(text[-(i+1)], end="")