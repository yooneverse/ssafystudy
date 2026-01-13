from collections import deque

n, w, l = map(int, input().split())
t = list(map(int, input().split()))

trucks = deque(t)

# w 다리의 길이
# l 다리의 최대 하중
bridge = deque([0] * w) 
weight = 0
time = 0

while bridge: # 다리에 뭔가 있으면 계속 해라
    
    weight -= bridge.popleft() # 우선 젤 왼쪽에 있는걸 지우고
    if trucks:
        if trucks[0] + weight <= l:

            truck = trucks.popleft()
            bridge.append(truck)
            weight += truck
        
        else:
            bridge.append(0)
    
    # print(f"{time} : {bridge}")    
    time += 1
    
print(time)