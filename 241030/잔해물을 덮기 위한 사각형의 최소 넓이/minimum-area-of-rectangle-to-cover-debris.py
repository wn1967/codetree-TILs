# array = [[0]*2001 for _ in range(2001)]
# OFFSET = 1000

# x1, y1, x2, y2 = map(int, input().split())
# x3, y3, x4, y4 = map(int, input().split())


# for z in range(x1+OFFSET,x2+OFFSET):
#     for x in range(y1+OFFSET,y2+OFFSET):
#         if (x1+OFFSET and y1+OFFSET) or (x2+OFFSET  and y2+OFFSET) < 0:
#             x -= 1
#             z -= 1
#             array[z][x] += 1
#         else:
#             array[z][x] += 1
    
# for z in range(x3+OFFSET,x4+OFFSET):
#     for x in range(y3+OFFSET,y4+OFFSET):
#         if (x3+OFFSET and y3+OFFSET) or (x4+OFFSET  and y4+OFFSET):
#             x -= 1
#             z -= 1
#             array[z][x] = 0
#         else:
#             array[z][x] = 0


# blank = []
# for a in range(2001):
#     count = 0
#     for b in range(2001):
#         if array[a][b] >= 1:
#             count += 1
#     blank.append(count)

# blank2 = []
# for c in range(2001):
#     count2 = 0
#     for d in range(2001):
#         if array[d][c] >= 1:
#             count2 += 1
#     blank2.append(count2)

# print(max(blank)*max(blank2))

def get_min_area(rect1, rect2):
    """
    두 직사각형이 주어졌을 때, 두 번째 직사각형에 의해 덮이지 않은 첫 번째 직사각형의 나머지 부분을 완전히 덮는 최소 직사각형의 넓이를 구합니다.

    Args:
        rect1 (list): 첫 번째 직사각형의 좌측 하단과 우측 상단 좌표 (x1, y1), (x2, y2)
        rect2 (list): 두 번째 직사각형의 좌측 하단과 우측 상단 좌표 (x1, y1), (x2, y2)

    Returns:
        int: 최소 직사각형의 넓이
    """

    # 겹치는 부분의 좌표 계산
    overlap_left = max(rect1[0], rect2[0])
    overlap_bottom = max(rect1[1], rect2[1])
    overlap_right = min(rect1[2], rect2[2])
    overlap_top = min(rect1[3], rect2[3])

    # 겹치지 않는 부분(잔해물)의 좌표 계산
    remainder_left = rect1[0]
    remainder_bottom = rect1[1]
    remainder_right = max(rect1[2], overlap_right)
    remainder_top = max(rect1[3], overlap_top)

    # 최소 직사각형의 넓이 계산
    width = remainder_right - remainder_left
    height = remainder_top - remainder_bottom
    return width * height

# 입력 받기
rect1 = list(map(int, input().split()))
rect2 = list(map(int, input().split()))

# 최소 직사각형 넓이 계산 및 출력
result = get_min_area(rect1, rect2)
print(result)