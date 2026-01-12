#무방향 연결 그래프에서 모든 정점을 연결하면서 간선 가중치 합이 최소가 되는 트리


import sys
sys.setrecursionlimit(10**6)
# 가중치가 음수가 나올 수 있으므로 다익스트라 불가
# 크루스칼 방식
def find_set(x):
    #정점 x가 속한 집합(트리)의 대표를 찾는다.
    #x에서 루트까지 올라가는 경로상의 모든 노드의 부모를 루트로 바로 연결
    if x == parents[x]:
        return x

    # x가 자신의 부모면, x는 그 집합의 루트(대표)
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return     # 이미 같은 집합이면 아무 것도 하지 않음


    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry


V, E = map(int, input().split())  #V : 정점 수  E : 간선의 수

edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

edges.sort(key=lambda x: x[2])  #가중치를 오름차순으로 정렬
                                # 크루스칼은 정렬이 필수

cnt = 0     # 현재까지 선택한 간선 수
cnt_w = 0   # 가중치의 합
parents = [i for i in range(V + 1)]

for A, B, C in edges:
    if find_set(A) != find_set(B): #A와 B의 루트가 다르면 서로 다른 연결요소
        union(A, B)
        cnt += 1
        cnt_w += C

    if cnt == V-1:
        break

print(cnt_w)
