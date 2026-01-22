import sys
input = sys.stdin.readline

def brute(num, p, k):
    global answer

    if p == N - 1 or k == M:
        answer = max(num, answer)
        return

    brute(num + snow[p + 1], p + 1, k + 1)
    if p + 2 <= N - 1:
        brute(num // 2 + snow[p + 2], p + 2, k + 1)



N, M = map(int, input().split())
snow = list(map(int, input().split()))

answer = 0

brute(1, -1, 0)

print(answer)
