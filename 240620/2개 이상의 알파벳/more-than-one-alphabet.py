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


check(word)

if len(blank) >= 2:
    print('Yes')
else:
    print('No')