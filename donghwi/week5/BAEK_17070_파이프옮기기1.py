# fail 뜨고 있는 중

# {0: →, 1: ↘, 2: ↓} 순서로 탐색
def DFS(y, x, d):
    global cnt

    # 파이프 위치가 집(범위) 안에 들어있고 벽이 없는 곳 이라면
    if lst[y][x] == 1 or y >= N and x >= N:
        return

    # 목표에 도착하면 이동 가능한 방법의 수 +1
    if (y, x) == (N - 1, N - 1):
        if d == 1:
            if lst[y - 1][x] == 0 and lst[y][x - 1] == 0:
                cnt += 1
                return
        else:
            cnt += 1
            return

    # 파이프가 가로로 놓아져 있다면
    if d == 0:
        # →, ↘ 방향 순서로 이동
        DFS(y, x + 1, 0)
        DFS(y + 1, x + 1, 1)
    # 파이프 방향이 대각선으로 놓아져 있다면
    elif d == 1:
        # 3칸의 공간이 반칸이어야 이동 가능
        if lst[y - 1][x] == 1 or lst[y][x - 1] == 1:
            return
        # →, ↘, ↓ 방향 순서로 이동
        else:
            DFS(y, x + 1, 0)
            DFS(y + 1, x + 1, 1)
            DFS(y + 1, x, 2)
    # 파이프 방향이 세로로 놓아져 있다면
    else:
        # ↘, ↓ 방향 순서로 이동
        DFS(y + 1, x + 1, 1)
        DFS(y + 1, x, 2)


N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

DFS(0, 1, 0)

print(cnt)
