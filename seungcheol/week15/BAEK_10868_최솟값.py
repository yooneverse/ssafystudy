import sys, math
input = sys.stdin.readline

N, M = map(int, input().split())
row = math.floor(math.log2(N))
table = [[0] * N for _ in range(row + 1)]

for i in range(N):
    table[0][i] = int(input().strip())

for r in range(1, row + 1):
    for c in range(0, N - 2 ** r + 1):
        table[r][c] = min(table[r - 1][c], table[r - 1][c + 2 ** (r - 1)])

for j in range(M):
    a, b = map(int, input().split())
    k = math.floor(math.log2(b - a + 1))
    print(min(table[k][a - 1], table[k][b - 2 ** k]))

# for t in table:
#     print(t)
