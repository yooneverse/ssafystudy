def recur(idx, matrix):
    global min_result

    if idx == K:
        search(matrix)
        return

    for i in range(K):

        if visited[i]:
            continue

        visited[i] = 1
        recur(idx + 1, rounding(round[i], matrix))
        visited[i] = 0

    return


def rounding(edge, mat):
    r, c, s = edge

    new_mat = [row[:] for row in mat]

    for layer in range(1, s + 1):
        top, left = r - layer, c - layer
        bottom, right = r + layer, c + layer

        # 상단 행: (top, left..right-1) -> (top, left+1..right)
        for j in range(left + 1, right + 1):
            new_mat[top][j] = mat[top][j - 1]

        # 우측 열: (top..bottom-1, right) -> (top+1..bottom, right)
        for i in range(top + 1, bottom + 1):
            new_mat[i][right] = mat[i - 1][right]

        # 하단 행: (bottom, right..left+1) -> (bottom, right-1..left)
        for j in range(right - 1, left - 1, -1):
            new_mat[bottom][j] = mat[bottom][j + 1]

        # 좌측 열: (bottom..top+1, left) -> (bottom-1..top, left)
        for i in range(bottom - 1, top - 1, -1):
            new_mat[i][left] = mat[i + 1][left]

    return new_mat


def search(arr):
    global min_result

    # for i in range(1, N + 1):
    #     for j in range(1, M + 1):
    #         print(arr[i][j],end=" ")
    #     print()
    #
    # print()

    for i in range(1, N + 1):
        calcul = 0
        for j in range(1, M + 1):
            calcul += arr[i][j]
        min_result = min(min_result, calcul)

    return


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M, K = map(int, input().split())

min_result = float('inf')
visited = [0] * K

board_map = [list(map(int, input().split())) for _ in range(N)]
board = [[0] * (M + 1)]

for i in range(N):
    board.append([0] + board_map[i])

round = [tuple(map(int, input().split())) for _ in range(K)]

recur(0, board)

print(min_result)
