import sys
input = sys.stdin.readline

N = int(input().strip())

edges = []

for _ in range(N - 2):
    s, e = map(int, input().split())
    edges.append((s, e))

# make_set
p = list(range(N + 1))

def find_set(x):
    root = x

    while p[root] != root:
        root = p[root]

    while p[x] != x:
        parent = p[x]
        p[x] = root
        x = parent
    return root

def union(x, y):
    king_x = find_set(x)
    king_y = find_set(y)

    if king_x == king_y:
        return

    p[king_y] = king_x

for s, e in edges:
    if find_set(s) != find_set(e):
        union(s, e)


answer = find_set(1)
for i in range(1, N + 1):
    if answer != find_set(i):
        print(1, i)
        break
