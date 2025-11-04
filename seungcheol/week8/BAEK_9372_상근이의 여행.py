def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return 0

    if rank[rep_x] == rank[rep_y]:
        rank[rep_x] += 1
        parent[rep_y] = rep_x
    elif rank[rep_x] > rank[rep_y]:
        parent[rep_y] = rep_x
    else:
        parent[rep_x] = rep_y
    return 1

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    # make_set()
    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    answer = 0

    for _ in range(M):
        A, B = map(int, input().split())
        answer += union(A, B)

    print(answer)