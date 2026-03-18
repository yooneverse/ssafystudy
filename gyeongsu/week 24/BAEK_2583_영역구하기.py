from collections import deque

r, c, k = map(int, input().split())

field = [[0] * c for _ in range(r)]

for _ in range(k):
    
    # x1, y1, x2, y2 순으로 입력
    # x1 = c1, y1 = r1 으로 치환해서 풀이
    
    c1, r1, c2, r2 = map(int, input().split())
    
    # 사각형이 있는경우 필드를 1로 변경
    for cc in range(c1, c2):
        for rr in range(r1, r2):
            field[rr][cc] = 1
    
    


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[False] * c for _ in range(r)]

ans = []
for ri in range(r):
    for ci in range(c):
        if field[ri][ci]: continue
    
        dq = deque([])
        cnt = 1
        dq.append((cnt, ri, ci))
            
        field[ri][ci] = 1
        
        while dq:
            cost, rIdx, cIdx = dq.popleft()
            
            for i in range(4):
                nr = rIdx + dr[i]
                nc = cIdx + dc[i]
                
                if (0 <= nr < r and 0 <= nc < c and not field[nr][nc]):
                    cnt += 1
                    dq.append((cnt, nr, nc))
                    field[nr][nc] = 1
                    
        ans.append(cnt)
      
ans.sort()    
print(len(ans))          
print(*ans)
            
            
