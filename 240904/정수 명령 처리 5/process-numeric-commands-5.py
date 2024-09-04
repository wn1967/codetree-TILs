n = int(input())

blank = []
count = -1

for i in range(n):
    arr = list(input().split())
    
    if arr[0] == 'push_back':
        blank.append(int(arr[1]))
        count += 1
    # elif arr[0] == 'get':
    #     print(blank[count])
    elif arr[0] == 'get':
        k = int(arr[1]) - 1  # k는 1부터 시작하므로 0-index로 맞추기 위해 -1
        print(blank[k])
    elif arr[0] == 'pop_back':
        blank.pop()
        count -= 1
    elif arr[0]=='size':
        print(len(blank))