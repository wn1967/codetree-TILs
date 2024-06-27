word = input()
search = input()

def check(word, search):
    global result
    for i in range(len(word)-1):
        result = 0
        for j in range(len(search)):
            if word[i+j] == search[j]:
                result += 1        
    if result == len(search):
        print(i)
    elif result < len(search):
        print(-1)

check(word, search)