from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0] * w)   # 다리 위 상태
time = 0
idx = 0
cur = 0  # 현재 다리 위 총 무게

while idx < n or cur > 0:
    time += 1

    out = bridge.popleft()   # 다리 끝에서 내려감
    cur -= out

    # 다음 트럭 올릴 수 있으면 올리고 아니면 0(빈칸)
    if idx < n and cur + trucks[idx] <= L:
        bridge.append(trucks[idx])
        cur += trucks[idx]
        idx += 1
    else:
        bridge.append(0)

print(time)
