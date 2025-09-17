def pipe(s, e):
    global result

    # 기저조건: (N-1, N-1)에 도착하면 종료
    if e == (N-1, N-1):
        result += 1
        return

    r = e[0] - s[0]
    c = e[1] - s[1]
    # 오른쪽 이동
    if c:
        # 이동 가능한지 확인
        # 인덱스 범위 안 & 이동 반경에 벽이 없음
        if e[1] + 1 <= N-1 and matrix[e[0]][e[1] + 1] == "0":
            pipe(e, (e[0], e[1] + 1))

    # 아래 이동:
    if r:
        # 이동 가능한지 확인
        # 인덱스 범위 안 & 이동 반경에 벽이 없음
        if e[0] + 1 <= N - 1 and matrix[e[0] + 1][e[1]] == "0":
            pipe(e, (e[0] + 1, e[1]))

    # 오른쪽 대각선 아래 이동
    # 이동 가능한지 확인
    # 인덱스 범위 안 & 이동 반경에 벽이 없음
    if e[0] + 1 <= N-1 and e[1] + 1 <= N - 1 and matrix[e[0] + 1][e[1]] == "0" and matrix[e[0]][e[1] + 1] == "0" and matrix[e[0] + 1][e[1] + 1] == "0":
        pipe(e, (e[0] + 1, e[1] + 1))


N = int(input())

matrix = [list(input().split()) for _ in range(N)]

if matrix[N-1][N-1] == "1":
    print(0)
    exit()
result = 0

pipe((0, 0), (0, 1))

print(result)