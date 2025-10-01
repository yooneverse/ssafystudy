# BAEK 1197. 최소 스패닝 트리
import sys
sys.setrecursionlimit(100000)
# sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())

# Kruskal
# 입력값 저장할 경로 배열 설정
route = []
for _ in range(E):
    A, B, C = map(int, input().split())
    route.append((A, B, C))

# 가중치 오름차순으로 배열 정렬
route.sort(key=lambda x: x[2])

# make_set
p = list(range(V + 1))


def find_set(x):
    if p[x] == x:
        return x

    p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    rx, ry = find_set(x), find_set(y)

    if rx == ry:
        return

    if rx > ry:
        p[rx] = ry
    else:
        p[ry] = rx


best = cnt = 0

for a, b, c in route:
    if find_set(a) != find_set(b):
        union(a, b)
        cnt += 1
        best += c

        if cnt == V - 1:
            break

print(best)
