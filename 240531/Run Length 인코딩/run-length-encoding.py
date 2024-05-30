# text = input()
# count = 0

# before = ''
# blank = []
# for i in range(len(text)):
#     if before != text[i]:
#         blank.append(text[i])
#     if before == text[i]:
#         count += 1
    

#     before = text[i]
#     blank.append(count)
# print(blank)

text = input()
count = 1
result = ''
before = ''

for i in range(len(text)):
    if before == text[i]:
        count += 1
    else:
        if before:
            result += before + str(count)
        before = text[i]
        count = 1

# 마지막 문자 처리
if before:
    result += before + str(count)

print(len(result))
print(result)