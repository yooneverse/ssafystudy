from collections import deque

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]


# 찾고 싶은 답 -> 총 단지 수
apt = 0
# 델타로 찾기
delta = [[-1,0],[1,0],[0,-1],[0,1]]
visited = [[0]* N for _ in range(N)]


rose = []


# 1을 찾고 그 1이 이어질때까지 같은 번호를 더해준다
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1 and visited[r][c] == 0:
            q = deque()
            q.append([r, c])
            apt_cnt = 0
            while q:
                # 다음 갈 곳을 pop한다
                qr, qc = q.popleft()
                visited[qr][qc] = 1
                for dr, dc in delta:
                    nr = qr + dr
                    nc = qc + dc
                    if 0<=nr<N and 0<=nc<N and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                        visited[nr][nc] += 1
                        q.append((nr, nc))
                apt_cnt += 1
            rose.append(apt_cnt)



print(len(rose))
rose.sort()
for i in rose:
    print(i)