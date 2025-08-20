T = 10

# 연산자 우선순위
pri = {'*': 2, '+': 1}

# 중위표기식을 후위표기식으로 변환
def get_postfix(infix):
    postfix = ""
    stack = []

    for token in infix:
        if token not in "+*":   # 피연산자
            postfix += token
        else:  # 연산자
            while stack and pri[token] <= pri[stack[-1]]:
                postfix += stack.pop()
            stack.append(token)

    # 남은 연산자 pop
    while stack:
        postfix += stack.pop()

    return postfix


# 후위표기식 계산
def get_result(postfix):
    stack = []
    for token in postfix:
        if token not in "+*":
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()

            if token == '+':
                stack.append(left + right)
            elif token == '*':
                stack.append(left * right)

    return stack.pop()


for tc in range(1, T + 1):
    N = int(input())   # 식의 길이
    infix = input()    # 중위표기식

    postfix = get_postfix(infix)
    result = get_result(postfix)

    print(f"#{tc} {result}")

