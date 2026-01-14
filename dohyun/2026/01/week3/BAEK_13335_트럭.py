# BAEK 13335. 트럭
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# n 개의 트럭, 다리 위에는 w 개의 트럭이 동시에 올라갈 수 있음(다리의 길이: w)
# 트럭들은 하나의 단위 시간에 하나의 단위 길이만큼 이동
# 다리가 견딜 수 있는 최대 하중은 L

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
time = weight = idx = 0

# 빈 다리위를 0으로 채움
bridge = deque([0] * w)

while idx < n or weight > 0:
    time += 1
    weight -= bridge.popleft()
    if idx < n:
        if weight + trucks[idx] <= L:
            bridge.append(trucks[idx])
            weight += trucks[idx]
            idx += 1
        else:
            bridge.append(0)

print(time)
