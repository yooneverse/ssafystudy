import sys

T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    result = 0
    for i in range((N // 3) + 1):
        a = N - (3 * i)
        result += a // 2 + 1

    print(result)