from collections import deque

def brute(cnt, lst):
    global answer
    if cnt > N // 2:
        answer = max(answer, cal(lst))
        return

    for idx in range(cnt, N // 2):
        lst.append(idx)
        brute(idx + 2, lst)
        lst.pop()
    brute(N // 2 + 2, lst)

def cal(lst):
    olst = deque(lst)
    length = (N - 2 * len(olst))
    tmp_ex = [None] * length
    tmp_idx = 0
    flag = -1
    ex_idx = 0
    while tmp_idx < length:
        if flag == -1 and olst:
            flag = olst.popleft()
        if ex_idx == flag * 2:
            flag = -1
            if expression[ex_idx + 1] == '+':
                tmp_ex[tmp_idx] = int(expression[ex_idx]) + int(expression[ex_idx + 2])
            elif expression[ex_idx + 1] == '-':
                tmp_ex[tmp_idx] = int(expression[ex_idx]) - int(expression[ex_idx + 2])
            else:
                tmp_ex[tmp_idx] = int(expression[ex_idx]) * int(expression[ex_idx + 2])
            ex_idx += 3
            tmp_idx += 1
        else:
            if expression[ex_idx] in ('+', '-', '*'):
                tmp_ex[tmp_idx] = expression[ex_idx]
            else:
                tmp_ex[tmp_idx] = int(expression[ex_idx])
            ex_idx += 1
            tmp_idx += 1

    result = tmp_ex[0]
    for j in range(1, len(tmp_ex), 2):
        o, n = tmp_ex[j:j + 2]
        if o == '+':
            result += int(n)
        elif o == '-':
            result -= int(n)
        else:
            result *= int(n)
    return result

N = int(input())
expression = input()

answer = -float('inf')

brute(0, [])

print(answer)
