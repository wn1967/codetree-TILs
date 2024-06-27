word = input()
search = input()

def check(word, search):
    result = -1  # 초기값을 -1로 설정
    for i in range(len(word) - len(search) + 1):  # 검색 범위 조정
        match_count = 0
        for j in range(len(search)):
            if word[i + j] == search[j]:
                match_count += 1
            else:
                break  # 일치하지 않으면 중지
        if match_count == len(search):
            result = i
            break  # 일치하는 첫 번째 위치를 찾으면 중지

    print(result)

check(word, search)