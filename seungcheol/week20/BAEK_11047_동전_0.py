import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin = []
for i in range(n):
    tmp = int(input().strip())
    coin.append(tmp)

coin.sort(reverse=True)

answer = 0
for c in coin:
    if c <= k:
        tmp = k // c
        answer += tmp
        k -= c * tmp

print(answer)
