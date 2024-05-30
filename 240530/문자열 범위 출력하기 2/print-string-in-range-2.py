text = input()
n = int(input())

if len(text) > n:
    for i in range(n):
        print(text[-(i+1)], end="")
else:
    print(text)