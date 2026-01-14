'''
다리 위 트럭
선입 선출
큐를 사용한 풀이가 더 효율적일까?

다리를 덱으로
트럭 이동 방식: 에스컬레이터? 트럭이 없어도 빈 칸을 두어서 다리 길이를 유지
'''
'''
결과
메모리 34916 KB
시간 60 ms
'''
from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

# 다리 위 트럭 (나가는 시간, 무게) 를 저장
bridge = deque([0]*w)
# 다리 위 무게
weight = 0
# 총 시간
time = 0

# 1초마다 한 칸씩 이동한다고 생각
# 도착 칸에 트럭이 없는 경우 무게는 0만큼 추가

# 다리 위에 트럭이 있는 동안
while bridge:
    # 1초 후
    time += 1
    # 도착한 트럭의 무게 (트럭 없는 칸이면 0)
    arrive = bridge.popleft()
    weight -= arrive

    # 건너지 못하고 남은 트럭이 있다면
    if trucks:
        # 다음으로 이동할 트럭의 무게 확인
        if weight + trucks[0] <= L:
            # 남은 트럭 리스트에서 빼냄
            start = trucks.popleft()
            # 다리 위에 추가
            bridge.append(start)
            weight += start
        # 무게가 다리 하중 초과한다면 무게 0을 올림
        else:
            bridge.append(0)

print(time)

