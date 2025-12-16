'''
N x N 도시 

치킨 거리 = 각 집에서 치킨집까지 최소 거리 총합

현존하는 치킨 집 중 M 개만 남김
치킨 거리의 최솟값 구하기



'''

import sys
input = sys.stdin.readline

# 치킨집 선택
def choice(idx, now, cnt):
    # M개 선택됐으면 치킨 거리 계산
    if cnt == M:
        cal(now)
        return
    # M개 선택 못했는데 마지막 치킨집까지 왔다면 종료
    if idx == t_chi:
        return

    # idx번째 치킨집 선택
    choice(idx+1, now+[chicken[idx]], cnt+1)
    # idx번째 치킨집 선택X
    choice(idx+1, now, cnt)


def cal(chi):
    global ans
    result = 0
    # 각 집에 대해서
    for x,y in house:
        d = float('inf')

        # 각 치킨집까지 최소 거리 
        for a,b in chi:
            dist = abs(a-x)+abs(b-y)

            if dist == 1:
                d= min(d,dist)
                break
            d = min(d,dist)

        result += d
        if result >= ans:
            return
    ans = result
    return


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []

# 각 집과 치킨집 위치 정리
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i,j))
        elif board[i][j] == 2:
            chicken.append((i,j))

t_chi = len(chicken)
ans = float('inf')
choice(0,[],0)
print(ans)