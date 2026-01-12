# 입력: C(가로, x), R(세로, y)
C, R = map(int, input().split())
K = int(input())

# 좌석 수보다 K가 크면 배정 불가
if K > C * R:
    print(0)
else:
    # 방문 여부
    visited = [[0] * (C + 1) for _ in range(R + 1)]

    # 방향: 위(0,1) → 오른쪽(1,0) → 아래(0,-1) → 왼쪽(-1,0)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0  # 현재 방향 인덱스

    # 시작 좌표 (1,1)이 1번
    x, y = 1, 1

    # 1번은 이미 배정된 상태이므로 K-1번만 이동하면 K번째 좌석
    for _ in range(1, K):
        visited[y][x] = 1  # 현재 좌석을 방문 처리

        nx = x + dirs[d][0]
        ny = y + dirs[d][1]

        # 다음 칸이 범위 밖이거나 이미 방문이라면 방향 전환
        if not (1 <= nx <= C and 1 <= ny <= R) or visited[ny][nx]:
            d = (d + 1) % 4
            nx = x + dirs[d][0]
            ny = y + dirs[d][1]

        x, y = nx, ny

    # 정답 출력: x y (x는 좌→우, y는 아래→위 증가)
    print(x, y)