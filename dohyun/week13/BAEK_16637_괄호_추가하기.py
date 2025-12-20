# BAEK 16637. 괄호 추가하기
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = input()

# 0 ~ 9, +, -, *
# 연산자 우선순위는 동일함
# 괄호 먼저 계산, 괄호 안에는 하나의 연산자
# 괄호 중첩 불가
# 결과의 최댓값 구하기


def operate(a, op, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    return a * b


def dfs(cnt, res):
    global best
    if cnt == len(ops):
        best = max(best, res)
        return

    dfs(cnt + 1, operate(res, ops[cnt], nums[cnt + 1]))
    if cnt + 1 < len(ops):
        temp = operate(nums[cnt + 1], ops[cnt + 1], nums[cnt + 2])
        dfs(cnt + 2, operate(res, ops[cnt], temp))


nums = [int(arr[i]) for i in range(0, N, 2)]
ops = [arr[i] for i in range(1, N, 2)]
best = -(2 ** 31)

dfs(0, nums[0])
print(best)
