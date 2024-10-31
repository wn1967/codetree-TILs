# N = int(input())
# blank = []
# for i in range(N):
#     aa = int(input())
#     blank.append(aa)

# blank2 = []

# cnt = 1
# for j in range(N):
    

#     if blank[j] ==0 or blank[j] == blank[j-1]:
#         cnt += 1


#     elif blank[j] != blank[j-1]:
#         cnt = 0

#     blank2.append(cnt)

#     print(blank2)    
def max_consecutive_numbers(numbers):
  max_count = 0
  current_count = 1
  for i in range(1, len(numbers)):
    if numbers[i] == numbers[i-1]:
      current_count += 1
    else:
      max_count = max(max_count, current_count)
      current_count = 1

  # 마지막 연속된 숫자를 처리
  max_count = max(max_count, current_count)

  return max_count

# 입력 받기
n = int(input())
numbers = [int(input()) for _ in range(n)]

# 최대 연속 횟수 계산 및 출력
result = max_consecutive_numbers(numbers)
print(result)