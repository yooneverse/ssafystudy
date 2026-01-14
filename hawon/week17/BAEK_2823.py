R, C = map(int, input().split())
road = [list(input().strip()) for _ in range(R)]

# 상하좌우
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for r in range(R):
    for c in range(C):
        if road[r][c] == '.':
            cnt = 0
            
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and road[nr][nc] == '.':
                    cnt += 1

            if cnt <= 1:
                print(1)
                exit()
print(0)