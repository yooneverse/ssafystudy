'''
3
3
7 3 4
5 8 2
1 9 6
4
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
5
25 14 6 24 5
11 8 16 17 1
12 3 2 22 15
19 7 21 9 18
10 4 13 23 20

#1 2
#2 11
#3 5
'''


TestCase = int(input())

for T in range(1, TestCase + 1):
    N = int(input())

    road = [list(map(int, input().split())) for _ in range(N)]

    # 상 -> 우 -> 하 -> 좌 순서로 탐색
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 최종 결과
    result = 0

    for i in range(N):
        for j in range(N):
            cnt = 0  # 이동 횟수 카운트
            y, x = i, j
            min_height = road[y][x]  # 탐색 후 최소값 을 찾기 위한 변수, 초기 설정은 탐색 시작점
            Go = True  # 인접한 영역에 갈 수 있는 갈 수 있다면 True, 없다면 False
            while Go:  # 인접한 영역에 갈 수 있다면
                cnt += 1  # 이동 횟수 +1
                Go = False
                # 디버깅용 출력문 (y좌표, x좌표), 현재 영역 값(value)
                # print(y, x, " ", road[y][x])
                for d in range(4):
                    nr = y + dr[d]
                    nc = x + dc[d]

                    # 등산로를 벗어나지 않으면서 탐색한 영역이 지금 까지 가장 낮다면
                    if 0 <= nr < N and 0 <= nc < N and min_height > road[nr][nc]:
                        min_height = road[nr][nc]  # 가장 작은 영역 갱신
                        min_y, min_x = nr, nc  # 가장 작은 영역 좌표 저장
                        Go = True  # 갈 수 있는 영역 찾아서 한번 더 탐색 할 수 있음

                y, x = min_y, min_x  # 가장 작은 영역 으로 이동

            result = max(result, cnt)  # 최대한 이동할 수 있는 값 갱신
            # print()

    print(f'#{T} {result}')