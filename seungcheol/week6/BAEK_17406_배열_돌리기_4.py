import copy

# gpt 풀이
# from collections import deque
# def rotate(matrix, r, c, s):
#     for sr in range(1, s + 1):
#         que = deque()
#
#         # 기존 내용 입력
#         # 상
#         for j in range(c - sr, c + sr):
#             que.append(matrix[r - sr][j])
#
#         # 우
#         for i in range(r - sr, r + sr):
#             que.append(matrix[i][c + sr])
#
#         # 하
#         for j in range(c + sr, c - sr, -1):
#             que.append(matrix[r + sr][j])
#
#         # 좌
#         for i in range(r + sr, r - sr, -1):
#             que.append(matrix[i][c - sr])
#
#         # 회전
#         que.rotate(1)
#
#         # 변경 내용 저장
#         for j in range(c - sr, c + sr):
#             matrix[r - sr][j] = que.popleft()
#
#         # 우
#         for i in range(r - sr, r + sr):
#             matrix[i][c + sr] = que.popleft()
#
#         # 하
#         for j in range(c + sr, c - sr, -1):
#             matrix[r + sr][j] = que.popleft()
#
#         # 좌
#         for i in range(r + sr, r - sr, -1):
#             matrix[i][c - sr] = que.popleft()
#
#     return matrix

# 최초 풀이
def sunyeol(n):
    global answer

    if n == K:
        matrix = copy.deepcopy(graph)
        for a in range(K):
            r, c, s = perm[a]
            matrix = rotate(matrix, r - 1, c - 1, s)

        for j in range(N):
            answer = min(answer, sum(matrix[j]))
        return

    for f in range(n, K):
        perm[n], perm[f] = perm[f], perm[n]
        sunyeol(n + 1)
        perm[n], perm[f] = perm[f], perm[n]


def rotate(matrix, r, c, s):
    for sr in range(1, s + 1):
        # 좌
        tmp = matrix[r - sr][c - sr]
        for il in range(r - sr, r + sr):
            matrix[il][c - sr] = matrix[il + 1][c - sr]

        # 상
        tmp2 = matrix[r - sr][c + sr]
        for it in range(c + sr, c - sr + 1, -1):
            matrix[r - sr][it] = matrix[r - sr][it - 1]
        matrix[r - sr][c - sr + 1] = tmp

        # 우
        tmp = matrix[r + sr][c + sr]
        for ir in range(r + sr, r - sr + 1, -1):
            matrix[ir][c + sr] = matrix[ir - 1][c + sr]
        matrix[r - sr + 1][c + sr] = tmp2

        # 하
        for ib in range(c - sr, c + sr - 1):
            matrix[r + sr][ib] = matrix[r + sr][ib + 1]
        matrix[r + sr][c + sr - 1] = tmp

    return matrix


N, M, K = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

perm = [list(map(int, input().split())) for _ in range(K)]

answer = float("inf")

sunyeol(0)

print(answer)
