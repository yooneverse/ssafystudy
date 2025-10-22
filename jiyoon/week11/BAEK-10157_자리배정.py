# 자리배정 (백준 10157)
# 달팽이 모양으로 좌석을 채워가면서
# K번째 사람의 위치를 구하는 문제

C, R = map(int, input().split())   # C: 가로(열), R: 세로(행)
K = int(input())                   # K: 찾고 싶은 번호

# 전체 좌석보다 K가 크면 자리 없음
if K > C * R:
    print(0)
    exit()

# 좌석판 (모두 0으로 초기화)
seat = [[0] * C for _ in range(R)]

# 이동 방향 (위 → 오른쪽 → 아래 → 왼쪽)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
move = 0     # 처음엔 위쪽으로 이동

# 시작 위치 (왼쪽 아래부터 시작)
x, y = 0, 0
num = 1      # 1번부터 시작

# 자리 채우기
while True:
    seat[y][x] = num  # 현재 위치에 번호 놓기

    # K번째 번호면 위치 출력하고 끝
    if num == K:
        print(x + 1, y + 1)   # (열, 행) 순서로 출력
        break

    # 다음 위치 계산
    nx = x + dx[move]
    ny = y + dy[move]

    # 다음 칸이 범위 밖이거나 이미 채워져 있으면 방향 바꾸기
    if nx < 0 or nx >= C or ny < 0 or ny >= R or seat[ny][nx] != 0:
        move = (move + 1) % 4     # 다음 방향으로 바꾸기
        nx = x + dx[move]
        ny = y + dy[move]

    # 실제 이동
    x, y = nx, ny
    num += 1
