import sys
sys.setrecursionlimit(10**6)
# 가중치가 음수가 나올 수 있으므로 다익스트라 불가
# 크루스칼 방식
def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry


V, E = map(int, input().split())

edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

edges.sort(key=lambda x: x[2])  #가중치를 오름차순으로 정렬
                                # 크루스은 정렬이 필수

cnt = 0     # 간선 수
cnt_w = 0   # 가중치의 합
parents = [i for i in range(V + 1)]

for A, B, C in edges:
    if find_set(A) != find_set(B):
        union(A, B)
        cnt += 1
        cnt_w += C

    if cnt == V:
        break

print(cnt_w)
