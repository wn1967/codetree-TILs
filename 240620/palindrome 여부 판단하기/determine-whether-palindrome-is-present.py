word = input()

def padd(word):
    result = 'True'

    for i in range(int(len(word)/2)):
        if word[i] == word[-(i+1)]:
            result = 'True'
        else:
            result = 'False'

    if result == 'True':
        print('Yes')
    else:
        print('No')

padd(word)