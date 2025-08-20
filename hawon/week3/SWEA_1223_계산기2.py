icp = {'+': 1, '*': 2}
isp = {'+': 1, '*': 2}

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = list(input().strip())

    # 3+4+5*6+7

    # 후위 표기식 만들기
    stack = []
    num = ''

    for token in arr:
        # 만약 token이 숫자면 num에 추가한다
        if token not in '+*':
            num += token
        # 만약 token이 연산자면
        else:
            # 2. 만약 스택이 있다면 top이랑 같거나 크면 다 꺼내 쓰기
            while stack and isp[stack[-1]] >= icp[token]:
                num += stack.pop()
            # 1. 추가하기
            stack.append(token)
    # for문 다 돌고 나서 남은 연산자가 있으면 pop
    while stack:
        num += stack.pop()

    # 이제 계산하기
    stack2 = []

    for i in num:
        # 숫자인 경우 stack에 넣어줌
        if i not in '+*':
            stack2.append(int(i))
        # 숫자 아니면
        else:
            # stack에서 숫자를 빼와서 계산해줘야함.
            # 대신 stack이 2개 이상일때
            if len(stack2) >= 2:
                one = stack2.pop()
                two = stack2.pop()
                if i == '+':
                    stack2.append(two + one)
                else:
                    stack2.append(two * one)
    answer = stack2.pop()
    print(f'#{tc} {answer}')