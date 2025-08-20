# 디지털 지도 N x M
# 높이 Hij
# 상하좌우보다 현재 위치가 높으면 안전지역
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Hij = [list(map(int, input().split())) for _ in range(N)]


    # 델타배열 상하좌우
    # [(-1,0),(1,0),(0,-1),(0,1)]

    # 안전구역의 수 변수로
    safe = 0

    for r in range(N):
        for c in range(M):
            # 지금 내위치
            now = Hij[r][c]
            big = 0
            # 델타배열 돌리기 이제 dr 하면 -1, dc 하면 0 이렇게 나올 예정
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if now > Hij[nr][nc]:
                        big += 1
                    if big == 4:
                        safe += 1
    print(f'#{tc} {safe}')