import sys

sys.setrecursionlimit(10000)

dp = [0] * 12  # dp[0]은 사용하지 않음


def add(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 4

    if dp[a] != 0:  # 이미 계산된 값이 있으면 재활용
        return dp[a]

    dp[a] = add(a - 1) + add(a - 2) + add(a - 3)
    return dp[a]


T = int(input())

for _ in range(T):
    N = int(input())
    print(add(N))
