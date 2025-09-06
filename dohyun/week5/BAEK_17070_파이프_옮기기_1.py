# BAEK 17070. 파이프 옮기기 1
# 1. 완전 탐색 버전
def pipe(row, col, d):  # 파이프 연결 함수
    global cnt  # 전역 변수(이동하는 경우의 수) 선언

    # 재귀 탈출 조건
    # (N - 1, N - 1) 에 도달하면 변수 증가 후 탈출
    if row == N - 1 and col == N - 1:
        cnt += 1
        return

    # 파이프 방향이 우, 대각일 때
    # 오른쪽으로 갈 수 있고, 그 칸이 1이 아니면 재귀 진행
    if d in [(0, 1), (1, 1)]:
        if col + 1 < N and home[row][col + 1] != 1:
            pipe(row, col + 1, (0, 1))

    # 파이프 방향이 하, 대각일 때
    # 아래쪽으로 갈 수 있고, 그 칸이 1이 아니면 재귀 진행
    if d in [(1, 0), (1, 1)]:
        if row + 1 < N and home[row + 1][col] != 1:
            pipe(row + 1, col, (1, 0))

    # 파이프 방향이 우, 하, 대각일 때
    # 대각으로 갈 수 있고, 우, 하, 대각방향 칸이 1이 아니면 재귀 진행
    if d in [(0, 1), (1, 0), (1, 1)]:
        if (row + 1 < N and col + 1 < N and
                home[row][col + 1] != 1 and
                home[row + 1][col] != 1 and
                home[row + 1][col + 1] != 1):
            pipe(row + 1, col + 1, (1, 1))


# 2. DP 버전
# ok 함수: (r, c 값이 범위 내인지 / 2차원 배열 값이 0인지) T/F 반환
def ok(r, c):
    return 0 <= r < N and 0 <= c < N and home[r][c] == 0

def dp(r, c, d):
    if r == N - 1 and c == N - 1:
        return  1

    ways = 0    # 반환할 결과값 변수

    # d: 우 = 0, 하 = 1, 대각 = 2
    # 만약 파이프가 우, 대각으로 향하면 오른쪽이 비어있으면 이동 가능
    if d in (0, 2) and ok(r, c + 1):
        # 파이프 방향 오른쪽
        ways += dp(r, c + 1, 0)

    # 만약 파이프가 하, 대각으로 향하고 아래쪽이 비어있으면 이동 가능
    if d in (1, 2) and ok(r + 1, c):
        # 파이프 방향 아래쪽
        ways += dp(r + 1, c, 1)

    # 만약 우, 하, 대각으로 비어있으면 대각 이동 가능
    if ok(r + 1, c) and ok(r, c + 1) and ok(r + 1, c + 1):
        # 파이프 방향 대각
        ways += dp(r + 1, c + 1, 2)

    return ways


N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
pipe(0, 1, (0, 1))

print(cnt)
print(dp(0, 1, 0))
