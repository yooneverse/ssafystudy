from collections import deque

N = int(input())                                                 # 게임 구역 가로 세로 길이 N
board = [list(map(int, input().split())) for _ in range(N)]      # 2차원 배열로 board 받아옴

def in_range(r, c):                                              # r과 c를 순회하며 범위를 지키도록 하는 함수
    return 0 <= r < N and 0 <= c < N                             # 범위 출력

visited = [[False] * N for _ in range(N)]                        # 2차원 배열로 확인해야 하기 때문에 모두 False인 배열 만들기

Q = deque()
Q.append((0, 0))
visited[0][0] = True

result = False
while Q:
    r, c = Q.popleft()                                           # 큐에서 현재 위치 꺼내기
    if (r, c) == (N - 1, N - 1):                                 # 오른쪽 아래 끝에 도달하면
        result = True                                            # 도달 가능하다는 표시 남기고
        break                                                    # 반복문 종료

    k = board[r][c]                                              # 현재 칸에 적힌 점프 거리 불러오기
    if k == 0:                                                   # 점프 거리가 0이면 더 이상 이동 불가
        continue                                                 # 다음 루프로 넘어감

    for nr, nc in [(r + k, c), (r, c + k)]:                      # 아래쪽, 오른쪽 방향으로 점프 시도
        if in_range(nr, nc) and not visited[nr][nc]:             # 범위 안이고 방문하지 않았다면
            visited[nr][nc] = True                               # 방문 처리하고
            Q.append((nr, nc))                                   # 큐에 추가

if result:                                                       # 탐색이 끝나고 도착했다면
    print("HaruHaru")                                            # 성공
else:                                                            # 도달하지 못했다면
    print("Hing")                                                # 실패



