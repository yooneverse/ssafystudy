'''
N * M 미로 (각각 100 이하 범위)
1*1 방으로 이루어짐

빈 방 or 벽
벽은 부숴야지 이동 가능

상하좌우 빈 방으로만 이동 가능 (미로 밖 이동 불가)

벽 평소 이동 불가. 무기로 부수기 가능

(1, 1)에서 (N, M)으로 이동하기 위해 부숴야 하는 최소 벽의 개수
'''
'''
최소 이동 거리가 아니라 부수는 벽의 최소 개수 

가능한 모든 경우의 수 확인해야 함

왔던 길을 되돌아갈 필요는 없음

가지치기 가능 요소
- 현재까지 찾은 부수는 벽의 최소 개수 이상이 되면 가지치기

'''
'''
무지성 dfs 풀이 시 메모리 초과 뜸

N, M 큰 경우 bfs 적용

새로운 아이디어 : 다익스트라, bfs

다익스트라 사용 가능 이유
- 출발점과 도착점이 고정되어 있음
- 부순 벽의 개수가 현재 최소를 넘어가면 더 이상 해당 경로는 필요 없음


bfs 사용 이유:
- 선입선출
- 현재 위치 기준으로 다음 위치 고려
- 다음 위치에 이전에 도달한 적 있다면 이전 경로에서 부순 벽의 개수 비교하여 큐 삽입 여부 판단


본 문제에서 dfs와 bfs 비교
- dfs는 목표지점까지 도착해야 함 >> 이후 더 나은 경로 생기면 또 끝까지 가야 함
- bfs는 기존 위치 근방부터 봄 >> 재방문 횟수 최소화
- bfs 사용 시, 목표 지점에 처음 도달하는 순간이 바로 최소 벽 파괴 횟수가 됨
- (항상 최소 벽 파괴횟수일 때만 큐에 넣어줄 것이기 때문)

'''
import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]
INF = float('inf')
broken_wall = [[INF]*M for _ in range(N)]
d = ((1,0), (-1,0), (0,1), (0,-1))

def solve():
    q = deque()
    # 시작 위치 0,0 / 현재까지 부순 벽 개수 0
    q.append((0,0,0))

    while q:
        cx, cy, wall = q.popleft()
        # 현재 위치까지 부순 벽의 개수가 지난 경로에서 부순 벽 개수 이상이면 더 이상 탐색X
        if broken_wall[cx][cy] <= wall:
            continue
        # 부순 벽 최소 개수 업데이트
        broken_wall[cx][cy] = wall

        for dx, dy in d:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < M:
                # 벽
                if maze[nx][ny] == '1':
                    if broken_wall[nx][ny] <= wall+1:
                        continue
                    else:
                        q.append((nx,ny,wall+1))
                # 빈 방
                elif maze[nx][ny] == '0':
                    if broken_wall[nx][ny] <= wall:
                        continue
                    else:
                        q.append((nx,ny,wall))


solve()
print(broken_wall[N-1][M-1])