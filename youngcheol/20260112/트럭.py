# 다리를 n개의 트럭이 건나가려고 한다. 
# 다리의 길이 W 
# 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야한다. 
# 먼저온 트럭이 다리위를 다지나가고 빠져나가는 것이라 큐를 사용
from collections import deque

def solve():

    n, w, L = map(int, input().split())

    truck = list(map(int, input().split()))
    bridge = deque([0] * w)
    
    current_weight = 0  # 현재 다리 위 트럭들의 무게 합
    time = 0           
    
   # 트럭이 오른쪽에 다없을때까지 반복
    while truck:
        time += 1 # 1
        
        #  다리를 다 건넌 트럭 빼자
        leaving_truck = bridge.popleft()
        current_weight -= leaving_truck
        
        # (현재 다리 무게 + 다음 트럭 무게) <= 최대 하중 L
        if current_weight + truck[0] <= L:
            new_truck = truck.popleft() 
            bridge.append(new_truck)   
            current_weight += new_truck  
        else:
  
            bridge.append(0)
            
    time += w
    
    # 맨마지막 시간 계산 
    print(time)

