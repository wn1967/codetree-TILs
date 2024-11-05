# N,M = map(int, input().split())
# check1 = []
# check11 = []
# check2 = []
# check22 = []

# start = 1000
# count = 0
# for i in range(N):
#     d, t = input().split()
#     t = int(t)
#     for j in range(1,t+1):
#         if d == 'R':
#             start += 1
#             check1.append(start)
#             count += 1
#             check11.append(count)
#         else:
#             start -= 1
#             check1.append(start)
#             count += 1
#             check11.append(count)

# start = 1000
# count = 0

# for i in range(M):
#     d, t = input().split()
#     t = int(t)
#     for j in range(1,t+1):
#         if d == 'R':
#             start += 1
#             check2.append(start)
#             count += 1
#             check22.append(count)
#         else:
#             start -= 1
#             check2.append(start)
#             count += 1
#             check22.append(count)
# result  = 0
# answer = 0
# for z in range(len(check11)):
#     if check1[z] == check2[z]:
#         result = 1
#         answer = z+1
#         break
#     else:
#         result = -1     

# if result == 1:
#     print(answer)
# else:
#     print(-1)

N, M = map(int, input().split())
A_moves = []
B_moves = []

for _ in range(N):
    d, t = input().split()
    t = int(t)
    A_moves.append((d, t))

for _ in range(M):
    d, t = input().split()
    t = int(t)
    B_moves.append((d, t))

A_pos = B_pos = 1000
time_A = time_B = 0

A_path = {}
B_path = {}

for d, t in A_moves:
    for _ in range(t):
        A_pos += 1 if d == 'R' else -1
        time_A += 1
        A_path[time_A] = A_pos

for d, t in B_moves:
    for _ in range(t):
        B_pos += 1 if d == 'R' else -1
        time_B += 1
        B_path[time_B] = B_pos

meeting_time = -1
for t in A_path:
    if A_path[t] == B_path.get(t):
        meeting_time = t
        break

print(meeting_time)