def check_parentheses(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:  # 스택이 비어있으면 잘못된 문자열
                return "No"
            stack.pop()  # 스택에서 '('를 하나 꺼냄
    
    if stack:  # 스택에 남아있다면 여는 괄호가 닫히지 않은 상태
        return "No"
    return "Yes"

# 입력 받기
s = input()

# 결과 출력
print(check_parentheses(s))