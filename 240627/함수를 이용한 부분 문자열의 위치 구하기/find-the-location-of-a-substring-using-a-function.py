word = input()
search = input()

def check(word, search):
    global result
    for i in range(len(word) - len(search) + 1): 
        result = 0
        for j in range(len(search)):
            if word[i+j] == search[j]:
                result += 1  
        key = result      
    if key == len(search):
        print(i)
    elif key < len(search):
        print(-1)

check(word, search)