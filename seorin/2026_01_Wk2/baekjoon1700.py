N, K = map(int, input().split()) # 멀티탭 구멍 개수, 사용 횟수  

names = list(map(int, input().split())) 

plugs = [] # 콘센트 관리 
result = 0

for i in range(K):
    # 1) 이미 동일한 게 꽂혀있으면 패스
    if names[i] in plugs:
        continue
    
    # 2) 만약 콘센트가 비어있다면 그냥 추가 
    if len(plugs) < N :
        plugs.append(names[i])
        continue
        
    # 3) 플러그가 다 찼을 경우 
    # 가정 : 뒤에 한 번도 안 나온다면  ? -> 제거 
    # 모두 나오면 가장 늦게 나오는 거 제거

    last = -1
    target = -1 # 뽑을 애

    for plug in plugs:
        if plug not in names[i+1:]:
            target = plug
            break

        else:
            nxt = names[i+1:].index(plug)
            if nxt > last:
                last = nxt
                target = plug

    plugs.remove(target)
    plugs.append(names[i])
    result += 1

print(result)