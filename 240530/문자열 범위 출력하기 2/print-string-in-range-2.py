text = input()
n = int(input())

for i in range(n):
    if len(text) > n:
        print(text[-(i+1)], end="")
    else:
        print(text)