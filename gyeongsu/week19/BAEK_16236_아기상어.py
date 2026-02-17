from collections import deque

n = int(input())

Map = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1,0), (0, -1), (0,1), (1,0)]


def bfs(sr, sc, size):
    q = deque()
    q.append((sr, sc, 0))

    visited = [[False] * n for _ in range(n)]
    visited[sr][sc] = True
    cost = 0
    min_cost = n*n+1
    
    candidate = []
    while q:
        
        r, c, cost = q.popleft()
        
        if cost >= min_cost:
            return candidate[0][0], candidate[0][1], min_cost

        for dr, dc in directions:
            nr , nc = r + dr, c + dc
        
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                
                if Map[nr][nc] > size:
                    continue
                
                if 0 < Map[nr][nc] < size:
                    min_cost = cost+1
                    candidate.append((nr, nc))
                    candidate.sort()
                    
                
                visited[nr][nc] = True
                q.append((nr,nc,cost+1))
                
            
                

    return -1, -1, -1

exp = 0
size = 2
for i in range(n):
    for ii in range(n):
        if Map[i][ii] == 9:
            sr, sc = i ,ii
            Map[i][ii] = 0

ans = 0

while True:
    nr, nc, dist = bfs(sr, sc, size)
    # print(f'{nr+1}, {nc+1}, 먹이 사이즈 {Map[nr][nc]}, 이동거리 {dist}, 먹는 순간 크기 {size}', end=' ')
    
    if dist == -1:
        break
    
    ans += dist
    exp += 1
    Map[nr][nc] = 0
    sr, sc = nr, nc
    
    
    if exp == size:
        size += 1
        exp = 0
    
    # print(ans)
    
print(ans)
                
                