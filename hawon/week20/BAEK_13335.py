from collections import deque

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

# 다리 상태 : 길이 w (처음엔 전부 0)
bridge = deque([0] * w)

# 전체 시간
time = 0        
# 현재 다리 위 무게
now_weight = 0
# 아직 안 올라간 트럭 인덱스
idx = 0

# 트럭이 남아있거나, 다리 위에 트럭이 남아있으면 계속
while idx < n or now_weight > 0:
    time += 1

    # 1초 경과 → 맨 앞 트럭(또는 0) 내려감
    out = bridge.popleft()
    now_weight -= out

    # 다음 트럭을 올릴 수 있는지 확인
    if idx < n and now_weight + trucks[idx] <= l:
        bridge.append(trucks[idx])
        now_weight += trucks[idx]
        idx += 1
    else:
        bridge.append(0)

print(time)
