def find_vps(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping.values():   # 여는 괄호
            stack.append(char)
        elif char in mapping:          # 닫는 괄호
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack   # 스택이 비어야 올바른 괄호 문자열


T = int(input())  # 테스트케이스 수 입력
for _ in range(T):
    s = input()  # 문자열 입력
    if find_vps(s):
        print("YES")
    else:
        print("NO")