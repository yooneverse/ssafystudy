# 우선순위 정하기
pri = {'+': 1, '*': 2}


# 중위 표현식에서 후위 표현식으로 바꾸기 위한 함수
def pos(tokens):
    stack = []  # 최종 연산식을 위한 스택
    oper_stack = []  # 연산자를 임시로 놔둘 스택

    for token in tokens:

        # 구성요소가 숫자인 경우
        if token.isdigit():
            stack.append(token)

        # 구성요소가 연산자일 경우
        else:

            # 토크보다 우선순위가 높거나 같은 연산자들을 위에서부터 stack으로 이동
            while oper_stack and pri[oper_stack[-1]] >= pri[token]:
                stack.append(oper_stack.pop())

            oper_stack.append(token)

    # 마지막 남은 연산자도 stack으로 이동동
    while oper_stack:
        stack.append(oper_stack.pop())

    return stack


# 만들어진 후위표현식을 계산
def get_result(tokens):
    stack = []

    # 만약 숫자일 경우 그대로 stack 에 담음
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))  # 계산식이다 보니까 int 활용


        # 만약 연산자인 경우 앞의 2개의 숫자를 꺼내 계산
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            if token == '+':  # 연산자 값이 +
                stack.append(num1 + num2)
            elif token == '*':  # 연산자 값이 *
                stack.append(num1 * num2)

    return stack[0]


for tc in range(1, 11):
    N = int(input())
    r = input()
    postfix = pos(r)
    result = get_result(postfix)
    print(f'#{tc} {result}')