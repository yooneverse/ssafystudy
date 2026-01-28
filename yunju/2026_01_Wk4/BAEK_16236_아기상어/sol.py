'''
문제
NN 사이즈 
2 <= N <= 20
4 <= N*N <= 400

처음 상어 사이즈 2
1초당 한 칸
상하좌우로 이동하며 물고기 먹으러 감 
이동 가능 칸: 상어 사이즈 이하
먹을 수 있는 물고기: 상어 사이즈 미만

본인 사이즈 개수만큼 물고기 먹으면 사이즈 커짐

먹을 수 있는 물고기 중 가장 가까운 물고기 먹으러 감
우선순위: 위 > 왼

먹을 수 있는 물고기가 없을 때까지 걸리는 시간 출력
'''
'''
아이디어

고려사항
1. 물고기의 사이즈가 상어보다 크면 해당 길로는 이동 불가
2. 물고기의 사이즈가 상어랑 같으면 먹을 수 없음

상어의 현 위치 기준으로 이동 가능한 칸과 거리를 고려해야 함
>> FIFO 큐를 이용

'''
from collections import deque


# 현재 위치에서 먹을 수 있는 물고기 탐색하는 함수
def bfs(sx, sy, size):
    # 상어의 방문 여부를 기록 (재방문 방지)
    # 상어로부터 거리를 기록
    visited = [[-1] * N for _ in range(N)]
    # 상어 이동 위치
    q = deque([(sx, sy)])
    # 처음 상어 위치
    visited[sx][sy] = 0
    
    # 물고기 후보군
    candidates = [] 

    while q:
        x, y = q.popleft()
        
        # 시간 단축
        # 먹을 수 있는 물고기 있는데, 지금 큐에서 꺼낸 위치가 더 멀다면 탐색 중지
        if candidates and visited[x][y] >= candidates[0][0]:
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 방문 여부 확인
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                # 상어 크기보다 작거나 같은 곳만 지나갈 수 있음
                if space[nx][ny] <= size:
                    # 이동 거리(시간) 기록
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                        
                    # 먹을 수 있다면 후보군에 추가
                    if 0 < space[nx][ny] < size:
                        candidates.append((visited[nx][ny], nx, ny))
    # 먹을 수 있는 물고기 있다면
    if candidates:
        # 거리, 행, 열 순으로 정렬하여 첫 물고기 먹기
        candidates.sort()
        return candidates[0]
    else:
        return None


N = int(input())
space = []

# 상어 위치
shark_x, shark_y = 0, 0
    
# 한 줄씩 입력받으며 상어 초기 위치 찾기
for i in range(N):
    row = list(map(int, input().split()))
    space.append(row)
    for j in range(N):
        if row[j] == 9:
            shark_x, shark_y = i, j
            space[i][j] = 0  # 상어의 시작 위치는 빈칸으로 변경

# 상어 상태
shark_size = 2
eat_cnt = 0

# 정답 시간
total_time = 0

# 상어 이동 방향
# 먹는 우선 순위: 위, 왼 
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

while True:
    # 잡아먹을 물고기 (거리, 행, 열)
    result = bfs(shark_x, shark_y, shark_size)
    # 없다면 끝
    if result is None: 
        print(total_time)
        break
        
    dist, nx, ny = result
        
    # 업데이트
    total_time += dist
    shark_x, shark_y = nx, ny
    space[nx][ny] = 0 # 물고기를 먹었으므로 빈칸 처리
    eat_cnt += 1
        
    # 먹은 물고기 수랑 상어 크기 같다면 
    # 상어 크기 1 키우고 먹은 물고기 0으로
    if eat_cnt == shark_size:
        shark_size += 1
        eat_cnt = 0
