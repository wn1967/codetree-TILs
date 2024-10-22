# N = int(input())
# blank = [1]*10000
# blank2= [1]*10000
# blank3= [1]*10000
# key = 5000

# for i in range(N):
#      A, B = input().split()
#     A = int(A)
#     if B == "R":
#         beforekey = key
#         key += A
#         for j in range(beforekey+101,key+101):
#             blank[j] = 2
#             blank2[j] += 1

#     elif B == "L":
#         beforekey = key
#         key -= A
#         for j in range(key+101,beforekey+101):
#             blank[j] = 3
#             blank3[j] += 1

# for g in range(len(blank)):
#     if blank2[g] >=3 and blank3[g]>=3:
#         blank[g] = 0

# wcount = 0
# bcount = 0
# gcount = 0

# for z in range(len(blank)):
#     if blank[z] == 3:
#         wcount += 1
#     elif blank[z] == 2:
#         bcount += 1
#     elif blank[z] == 0:
#         gcount += 1

# print(wcount, bcount, gcount)


# from collections import defaultdict

# def solve_tile_coloring():
#     N = int(input())
#     # 각 위치의 타일이 각각 흰색/검은색으로 칠해진 횟수를 저장
#     white_count = defaultdict(int)
#     black_count = defaultdict(int)
#     # 마지막으로 칠한 색을 저장 (1: 흰색, 2: 검은색)
#     last_color = defaultdict(int)
    
#     current_pos = 0  # 현재 위치
    
#     for _ in range(N):
#         x, direction = input().split()
#         x = int(x)
        
#         if direction == 'L':
#             # 왼쪽으로 이동하며 흰색으로 칠하기
#             end_pos = current_pos - x + 1
#             for i in range(current_pos, end_pos - 1, -1):
#                 white_count[i] += 1
#                 last_color[i] = 1
#             current_pos = end_pos
#         else:  # direction == 'R'
#             # 오른쪽으로 이동하며 검은색으로 칠하기
#             end_pos = current_pos + x - 1
#             for i in range(current_pos, end_pos + 1):
#                 black_count[i] += 1
#                 last_color[i] = 2
#             current_pos = end_pos
    
#     # 모든 칠해진 위치를 확인하여 색상 카운트
#     positions = set(white_count.keys()) | set(black_count.keys())
#     white = black = gray = 0
    
#     for pos in positions:
#         w_cnt = white_count[pos]
#         b_cnt = black_count[pos]
        
#         if w_cnt >= 2 and b_cnt >= 2:
#             gray += 1
#         elif last_color[pos] == 1:
#             white += 1
#         else:
#             black += 1
    
#     print(white, black, gray)

# solve_tile_coloring()

N = int(input())
white_count = [0]*20000  # 흰색으로 칠한 횟수
black_count = [0]*20000  # 검은색으로 칠한 횟수
last_color = [0]*20000   # 마지막으로 칠한 색 (1:흰색, 2:검은색)
current = 10000          # 시작 위치

for i in range(N):
    A, B = input().split()
    A = int(A)
    
    if B == "R":
        for j in range(current, current + A):
            black_count[j] += 1
            last_color[j] = 2
        current = current + A - 1
    else:  # B == "L"
        for j in range(current, current - A, -1):
            white_count[j] += 1
            last_color[j] = 1
        current = current - A + 1

white = black = gray = 0
colored_positions = set()

# 칠해진 위치만 확인하기 위해 먼저 찾기
for i in range(20000):
    if white_count[i] > 0 or black_count[i] > 0:
        colored_positions.add(i)

# 각 칠해진 위치의 최종 색상 결정
for pos in colored_positions:
    if white_count[pos] >= 2 and black_count[pos] >= 2:
        gray += 1
    elif last_color[pos] == 1:
        white += 1
    else:
        black += 1

print(white, black, gray)