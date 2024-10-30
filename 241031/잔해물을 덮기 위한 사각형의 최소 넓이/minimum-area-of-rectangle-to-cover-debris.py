array = [[0]*2001 for _ in range(2001)]
OFFSET = 1000

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# 첫 번째 직사각형 표시
for z in range(x1+OFFSET, x2+OFFSET):
    for x in range(y1+OFFSET, y2+OFFSET):
        array[z][x] = 1

# 두 번째 직사각형으로 덮이는 부분을 초기화
for z in range(x3+OFFSET, x4+OFFSET):
    for x in range(y3+OFFSET, y4+OFFSET):
        array[z][x] = 0

# 각 행에 대한 최대 연속 길이 확인
blank = []
for a in range(2001):
    max_row_length = 0
    current_length = 0
    for b in range(2001):
        if array[a][b] == 1:
            current_length += 1
            max_row_length = max(max_row_length, current_length)
        else:
            current_length = 0
    blank.append(max_row_length)

# 각 열에 대한 최대 연속 길이 확인
blank2 = []
for c in range(2001):
    max_col_length = 0
    current_length = 0
    for d in range(2001):
        if array[d][c] == 1:
            current_length += 1
            max_col_length = max(max_col_length, current_length)
        else:
            current_length = 0
    blank2.append(max_col_length)

print(max(blank) * max(blank2))