N = int(input())
tile_state = {}  # 타일 상태를 저장할 딕셔너리
current_pos = 0  # 현재 위치

for _ in range(N):
    x, direction = input().split()
    x = int(x)
    
    if direction == 'R':
        # 오른쪽으로 x칸 뒤집기
        for i in range(current_pos, current_pos + x):
            # 항상 해당 위치의 타일을 검은색(False)으로 변경
            tile_state[i] = False
        current_pos += x - 1  # 마지막 뒤집은 타일 위치로 이동
    
    else:  # direction == 'L'
        # 왼쪽으로 x칸 뒤집기
        for i in range(current_pos, current_pos - x, -1):
            # 항상 해당 위치의 타일을 흰색(True)으로 변경
            tile_state[i] = True
        current_pos -= x - 1  # 마지막 뒤집은 타일 위치로 이동

# 흰색(True)과 검은색(False) 타일 수 계산
white_count = sum(1 for state in tile_state.values() if state)
black_count = sum(1 for state in tile_state.values() if not state)

print(white_count, black_count)