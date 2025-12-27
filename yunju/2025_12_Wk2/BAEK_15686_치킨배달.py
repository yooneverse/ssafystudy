'''
문제 설명

N x N 크기의 도시 

여러 개의 집과 여러 개의 치킨 집이 존재

치킨 거리 = 각 집에서 치킨집까지 최소 거리 총합

현존하는 치킨 집 중 M 개만 남김

이 때 치킨 거리의 최솟값 구하기
'''
'''
아이디어

최소 거리를 알기 위해서는 
남길 M개의 치킨집에 대한 가능한 경우들을 구하고
각 경우마다 치킨 거리를 계산

2개의 함수 이용
>> M개의 치킨집을 선택하는 함수
>> M개의 치킨집이 주어졌을 때 치킨 거리 구하는 함수

'''
import sys
input = sys.stdin.readline

# 치킨집 선택
# idx: 치킨집 번호
# now: 현재까지 선택한 치킨집 리스트
# cnt: 현재까지 택한 치킨집 개수
def choice(idx, now, cnt):
    # M개 선택됐으면 치킨집 리스트 now를 치킨 거리 계산 함수로 보냄
    if cnt == M:
        cal(now)
        return
    # M개 선택 못했는데 마지막 치킨집까지 왔다면 종료
    if idx == t_chi:
        return

    # idx번째 치킨집 선택하는 경우
    choice(idx+1, now+[chicken[idx]], cnt+1)
    # idx번째 치킨집 선택하지 않는 경우
    choice(idx+1, now, cnt)

# 치킨 거리 계산 함수
# 치킨집 리스트를 받아와 각 가구에서 최소 거리를 계산
def cal(chi):
    # 최소 치킨 거리 (답)
    global ans
    # 총 치킨 거리
    result = 0

    # 각 집 좌표 (x,y)
    for x,y in house:
        # 집 별 최소 치킨집까지 거리 
        d = float('inf')

        # 각 치킨집까지 최소 거리 
        for a,b in chi:
            dist = abs(a-x)+abs(b-y)

            # 거리가 1이라면 이 경우가 최소이므로 다른 치킨집 볼 필요 없음
            if dist == 1:
                d= min(d,dist)
                break
            # 최소 거리 갱신
            d = min(d,dist)

        # 총 치킨 거리 갱신
        result += d

        # 현재 치킨거리보다 커지면 더 이상 계산 필요 없음
        # 가지치기
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

# 치킨집 개수
t_chi = len(chicken)

# 치킨 거리 초기 설정
# cal 함수를 통해 갱신될 예정 (답) 
ans = float('inf')

choice(0,[],0)
print(ans)