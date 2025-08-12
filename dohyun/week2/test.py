T = int(input())

# tc=test_case 불러오기
for tc in range(1, T+1):
    # 지도 별로 첫 줄에 N과 M이 공백으로 구분되어 주어짐
    N, M = map(int, input().split())

    # N*M 배열의 지도 만들기
    safe_map = [list(map(int, input().split())) * N for _ in range(N)]


    # 델타 (상, 하, 좌, 우)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    safe_cnt = 0  # 안전구역 수

    # 가장 자리는 인접 구역 정보가 부족하므로 제외 (1 ~ N-2, 1 ~ M-2)
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            safe = safe_map[i][j]  # 현재 칸의 높
            cnt = 0
            # 인접구역 탐색(상하좌우)
            for p in range(4):  # 인덱스 0~3: 상하좌우
                ni = i + di[p]
                nj = j + dj[p]
                # 중앙만 순회하므로 보통 경계 밖이 아니지만, 방어적으로 한 번 더 확인
                if 0 <= ni < N and 0 <= nj < M:
                    near = safe_map[ni][nj]  # 인접구역 높이
                    if near >= safe:         # 인접구역이 현재보다 높거나 같으면 안전구역 아님
                        # 여기서 불린 써야 할 거 같은데 어떻게 할지 모르겠다
                        cnt = -1

            if cnt != -1:
                safe_cnt += 1  # 안전구역 수 합산

    # 출력 형식 = #(지도번호) (안전구역 수)
    print(f"#{tc} {safe_cnt}")