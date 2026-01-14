import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, input().split())        # 트럭 수 n, 다리 길이 w, 최대 하중 L
trucks = deque(map(int, input().split())) # 대기 중인 트럭들

bridge = deque([0] * w)                   # 다리는 길이 w짜리 큐
current_weight = 0                        # 현재 다리 위 무게 합
time = 0                                  # 시간

while trucks:                             # 아직 못 올라간 트럭 있으면
    time += 1                             # 1초씩 더함

    out = bridge.popleft()                # 다리 한 칸 밀기 (앞에 있던 거 빠짐)
    current_weight -= out                 # 빠진 만큼 무게 빼기

    if current_weight + trucks[0] <= L:   # 다음 트럭 올려도 되면
        t = trucks.popleft()              # 트럭 하나 꺼내서
        bridge.append(t)                  # 다리 뒤에 올림
        current_weight += t               # 무게 추가
    else:                                 # 무게 때문에 못 올리면
        bridge.append(0)                  # 빈 칸 넣고 시간만 보냄

time += w                                 # 마지막 트럭 다리 끝까지 가는 시간
print(time)                               # 정답
