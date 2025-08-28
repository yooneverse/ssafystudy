T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 답 변수
    max_val = 0
    # 델타
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # 시작점 정하기 (돌아가면서)
    for r in range(N):
        for c in range(N):
            # 출발 좌표를 정한다
            sr, sc = r, c
            # 출발 좌표부터 세기
            cnt = 1

            while True:
            # 현재 위치가 제일 낮은 값이라고 가정
                min_r, min_c = sr, sc
                for dr, dc in delta:
                    nr = sr + dr
                    nc = sc + dc
                    # 최솟값 후보보다 더 낮으면 갱신
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] < arr[min_r][min_c]:
                        min_r, min_c = nr, nc
                # 이웃사촌 중에 제일 낮은 게 현재 위치보다 낮으면?
                if arr[sr][sc] > arr[min_r][min_c]:
                    sr, sc = min_r, min_c
                    cnt += 1
                # 안 낮으면
                else:
                    # 지금까지 셋던 max_val이랑 비교
                    if max_val < cnt:
                        max_val = cnt
                    # 종료하기
                    break

    print(f'#{tc} {max_val}')
