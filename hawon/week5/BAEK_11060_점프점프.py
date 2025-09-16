from collections import deque


def solve_bfs():
    N = int(input())
    arr = list(map(int, input().split()))

    # (현재 위치, 점프 횟수)
    q = deque()
    q.append((0,0))

    # 중복 방지를 위한 VISITED 배열 생성하기기
    visited = [0] * N
    visited[0] = 1

    while q:
        now, jumps = q.popleft()

        # 마지막 칸 도착 시 결과 반환
        if now == N - 1:
            print(jumps)
            return

        # 현재 위치에서 가능한 점프 탐색
        # arr[now] : 현재 위치에서 최대로 점프할 수 있는 거리
        for step in range(1, arr[now] + 1):
            # 다음 위치 계산
            nxt = now + step

            # 다음 위치가 미로의 범위를 벗어나지 않고, 아직 방문하지 않은 칸인지 확인
            if nxt < N and visited[nxt] == 0:
                visited[nxt] = 1

                q.append((nxt, jumps + 1))

    # 도착하지 못하면 -1
    print(-1)


solve_bfs()