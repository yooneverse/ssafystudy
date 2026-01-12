import sys
input = sys.stdin.readline


def swelling(x, y, z):
    if x + y <= z:
        return 0, x + y
    else:
        return x + y - z, z

def dfs(a, b, c):
    if (a, b, c) in visited:
        return
    visited.add((a, b, c))

    if a:
        x, y = swelling(a, b, B)
        dfs(x, y, c)

        x, y = swelling(a, c, C)
        dfs(x, b, y)

    if b:
        x, y = swelling(a, b, A)
        dfs(y, x, c)

        x, y = swelling(b, c, C)
        dfs(a, x, y)

    if c:
        x, y = swelling(a, c, A)
        dfs(y, b, x)

        x, y = swelling(b, c, B)
        dfs(a, y, x)

    return

A, B, C = map(int, input().split())

visited = set()
dfs(0, 0, C)

answer = []
for condition, _, water in visited:
    if condition:
        continue
    answer.append(water)

answer.sort()

print(*answer)
