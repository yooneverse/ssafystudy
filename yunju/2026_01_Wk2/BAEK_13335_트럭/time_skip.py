# 시간을 더 효율적으로 계산할 수 없을까?
# 어차피 각 트럭은 다리 위에 올라온 순간부터 w초 뒤에 건너감
# 무게 계산이 문제
# 어느 시점에 어떤 트럭이 나가고 무게가 어떻고

# 하중 꽉 찼다면 가장 앞 트럭이 나갈 때까지 아무 것도 못함
# 시간을 가장 앞 트럭이 나가는 시간으로 바꾸고 다음 트럭 모색

'''
결과
메모리 34924 KB
시간 56 ms
'''
from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

# 다리 위 트럭 (나가는 시간, 무게) 를 저장
bridge = deque()
weight = 0
time = 0

for truck in trucks:
    # 다리 위에 트럭 있고
    # 가장 앞 트럭이 다리에서 나가는 시간이 되었다면 내보내기
    if bridge and bridge[0][0] <= time:
        # 가장 앞 트럭 무게만큼 제거
        weight -= bridge.popleft()[1]

    # 다음 트럭
    # 최대하중 넘긴다면 다리 위에 있는 트럭이 나가야 함
    # 시간을 바로 트럭이 나가는 시간으로 변경
    while weight + truck > L:
        time = bridge[0][0]
        weight -= bridge.popleft()[1]

    # 다음 트럭 추가
    weight += truck
    # (트럭이 나가는 시간, 트럭 무게)
    bridge.append((time+w, truck))
    
    time += 1

print(time+w)

