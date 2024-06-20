word = input()
blank = []
def check(word):
    global result
    result = 'True'
    for i in word:
        if i in blank:
            result = 'False'
        else:
            blank.append(i)

    return result

check(word)

if result == 'False':
    print('Yes')
else:
    print('No')