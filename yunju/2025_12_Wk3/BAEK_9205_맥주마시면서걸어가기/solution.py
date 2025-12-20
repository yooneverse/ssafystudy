import sys
input = sys.stdin.readline

'''
문제 설명 

맥주 한 박스 (20 병)
50m에 한 병씩 마심
50m가기 위해서는 그 직전에 한 병 마셔야 갈 수 있음(연료)

맥주 추가 구매 가능성 유

편의점
빈 병 버리고 새 맥주 살 수 있음
박스에 맥주 병은 20 병 넘길 수 없음
편의점 나선 직후에도 50m 가기 전에 맥주 한 병 마셔야 함

페스티벌 도착 가능 여부 구하기
'''

'''
아이디어

도착 가능 여부는 어떻게 판단할 수 있을까?

출발지점 - 편의점 거리
편의점 - 편의점 거리
편의점 - 페스티벌 거리

맥주가 다 떨어지기 전에 편의점이나 페스티벌에 도착할 수 있어야 함

한 박스 20 병
20 * 50(m) = 1000(m)
한 박스로 1,000m 갈 수 있음

0 <= 편의점 개수 <= 100 

-32768 <= 각 지점 좌표 <= 32767
(
65535 (2^16-1)
16비트 정수형에 딱 맞게 담을 수 있도록 줌
메모리 최적화 암시(short), 일반적 정수형 범위 내에 충분히 들어옴
)
좌표 음수도 가능
숫자 자체가 크지는 않음. 


최소 방문 횟수 등과 같은 조건 없이 단순히 도달 가능 여부만 따지므로
경로 상에 있는 모든 편의점 방문해서 채우기

큐를 이용?
현재 위치에서 갈 수 있는 모든 편의점 탐색
방문했던 편의점으로 돌아가지는 말고

바운더리 내에 목적지가 들어온다면 도달 가능!

'''
from collections import deque

def cal_dist(now, goal):
    x = abs(now[0]-goal[0])
    y = abs(now[1]-goal[1])
    return x+y


def arrive():
    q = deque()
    q.append(home)

    while q:
        now_x, now_y = q.popleft()

        if cal_dist([now_x, now_y], festival) <= 1000:
            return True

        for nxt in range(n):
            if not visited[nxt]:
                if cal_dist([now_x, now_y], conveniences[nxt]) <= 1000:
                    q.append([conveniences[nxt][0], conveniences[nxt][1]])
                    visited[nxt] = 1


    return False




T = int(input())
for _ in range(T):
    # 편의점 개수
    n = int(input())
    home = list(map(int, input().split()))

    conveniences = []
    for _ in range(n):
        conveniences.append(list(map(int, input().split())))

    visited = [0]*n

    festival = list(map(int, input().split()))

    ans = arrive()

    if ans:
        print("happy")
    else:
        print("sad")


