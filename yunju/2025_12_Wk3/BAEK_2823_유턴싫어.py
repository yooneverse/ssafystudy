import sys
input = sys.stdin.readline
'''
문제 설명

R x C 마을
빌딩 X, 길 . 
네 방향 길로 이동 가능

임의의 한 길에서 출발
마을의 모든 구역을 돌아 시작 위치로 돌아올 수 있어야 함
단, 방금 이동한 방향의 반대 방향으로 이동은 불가(유턴 불가)

가능하다면 0
불가능하다면 1 
출력
'''
'''
아이디어

임의의 시작점이므로 . 인 지점 아무 곳에서 바로 시작
모든 길을 지나서 시작 자리로 돌아오기
지나간 길 재방문은 상관없음

중요점: 방향
그냥 직전 지점으로만 못 돌아가게 하면 될까?

직전 지점 제외, 나머지 세 방향 탐색
무한루프

3 <= R, C <= 10
범위가 아주 작음

모든 길을 다 방문해서 출발점으로 돌아왔다는 것을 어떻게 증명?

'''

'''
다른 생각

언제 막다른 길이 발생하는가

세 방향이 막힌 경우 (X 또는 벽으로)
방문 가능한 경로가 하나밖에 없다면!

'''

R, C = map(int, input().split())
road = [input().strip() for _ in range(R)]

dr = (1,0,-1,0)
dc = (0,-1,0,1)
def solve():
    for r in range(R):
        for c in range(C):
            if road[r][c] == '.':
                cnt = 0

                for d in range(4):
                    nr = r+dr[d]
                    nc = c+dc[d]
                    if 0<= nr < R and 0<= nc < C:
                        if road[nr][nc] == '.':
                            cnt += 1

                if cnt == 1:
                    print(1)
                    return
    print(0)
    return

solve()



