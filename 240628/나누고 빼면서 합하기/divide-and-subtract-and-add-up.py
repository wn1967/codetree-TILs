def check(n, m, array):
    result = 0
    while m > 1:
        result += array[m-1]
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2
    result += array[m-1]  # 마지막으로 m이 1일 때도 더해줘야 함
    print(result)

# 입력을 받습니다.
n, m = map(int, input().split())
array = list(map(int, input().split()))

# 함수 호출
check(n, m, array)