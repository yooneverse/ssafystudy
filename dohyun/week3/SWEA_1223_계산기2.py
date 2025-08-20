# 1223. [S/W 문제해결 기본] 6일차 - 계산기2
T = 10


def transform():
    N = int(input())
    string = input()
    stack = []
    trans_lst = []

    order = {'+': 1, '-': 1, '/': 2, '*': 2}

    for i in string:
        if i in '+-*/':
            if not stack or order[stack[-1]] < order[i]:
                stack.append(i)
            else:
                while order[stack[-1]] >= order[i]:
                    trans_lst.append(stack.pop())
                    if not stack:
                        break
                stack.append(i)
        else:
            trans_lst.append(i)

    while stack:
        trans_lst.append(stack.pop())

    return trans_lst


def cal(lst):
    target = lst
    stack = []

    for i in target:
        if i in '+-*/':
            if len(stack) > 1:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    stack.append(b + a)
                elif i == '-':
                    stack.append(b - a)
                elif i == '*':
                    stack.append(b * a)
                elif i == '/':
                    stack.append(b // a)
        else:
            stack.append(int(i))

    if len(stack) == 1:
        return stack.pop()


for tc in range(1, T+1):
    result = cal(transform())
    print(f'#{tc} {result}')
