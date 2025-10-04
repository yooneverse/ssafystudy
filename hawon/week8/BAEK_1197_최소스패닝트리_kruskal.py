# 최소 스패닝 트리 -> MST
# 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리

# 크루스칼
# 간선을 기준으로, 가중치를 오름차순으로 정렬
# UNION , 서로소 집합 활용

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    kx = find_set(x)
    ky = find_set(y)

    if kx == ky:   # 이미 같은 집합
        return False

    # rank가 낮은 트리를 높은 트리 밑에 붙인다
    if rank[kx] < rank[ky]:
        p[kx] = ky
    elif rank[kx] > rank[ky]:
        p[ky] = kx
    else:
        p[ky] = kx      # 아무 쪽이나 부모로 하고
        rank[kx] += 1   # 부모 트리 높이(rank) 1 증가
    return True


V, E = map(int, input().split())
graph = []
for _ in range(E):
    a, b, c = map(int, input().split())
    graph.append((c,a,b))


graph.sort()

# 부모 + rank 배열 초기화
p = [i for i in range(V+1)]
rank = [0] * (V+1)

cnt = 0
result = 0

for c, a, b in graph:
    if union(a,b):
        cnt += 1
        result += c

        if cnt == V-1:
            break

print(result)