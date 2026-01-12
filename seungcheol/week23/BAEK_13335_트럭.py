import sys
input = sys.stdin.readline

# queue 사용
from collections import deque

# 트럭 수, 다리 길이, 다리 최대 하중
n, w, l = map(int, input().split())

# 트럭 무게
truck = list(map(int, input().split()))

# 다리에 올라간 트럭의 무게 및 순서
bridge = deque([])

# 트럭 무게 인덱스, 다리위의 트럭 총 무게, 걸린 시간
idx = weight = answer = 0

# 아직 트럭이 다 못 올라갔거나 다리위에 트럭이 남아있으면 반복
while idx < n or bridge:
    # 매 반복마다 시간 경과
    answer += 1

    # 다리에서 트럭이 내려오는 기능
    if bridge and bridge[0][1] == answer - w:
        tw, _ = bridge.popleft()
        weight -= tw

    # 다리에 트럭이 올라가는 기능
    # 아직 안올라간 트럭이 있고,
    # 다리 길이보다 트럭수가 적고,
    # 다리의 최대하중보다 총 무게 + 다음 트럭 무게가 적으면
    if idx < n and len(bridge) < w and weight + truck[idx] <= l:
        weight += truck[idx]
        bridge.append((truck[idx], answer))
        idx += 1

print(answer)