import sys
input = sys.stdin.readline

"""
네 칸 합 
지나온 칸 1회 돌아가기 가능
단, 이 때는 합에 더하지 않음

"""

def find(i,j, cnt, num, perm, visited):
    global ans
    if cnt == 4:
        if num > ans:
            ans = num

        return

    for di, dj in ((0,1),(0,-1),(-1,0),(1,0)):
        ni, nj = i+di, j+dj
        if 0<= ni < N and 0<= nj < M:
            if visited[ni][nj] == True:
                if perm == 1:
                    continue
                else:
                    find(ni,nj,cnt,num,1,visited)
            else:
                visited[ni][nj] = True
                find(ni,nj,cnt+1,num+board[ni][nj],perm,visited)
                visited[ni][nj] = False



N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
visited = [[False]*M for _ in range(N)]
for x in range(N):
    for y in range(M):
        visited[x][y] = True
        find(x,y,1,board[x][y],0,visited)
        visited[x][y] = False
print(ans)