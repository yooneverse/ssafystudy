T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # k = 최대 이동 수, n = 이동 거리, m = 충전소 개수
    k, n, m = map(int, input().split())
    chargers = list(map(int, input().split()))
 
    # 충전기가 표시된 인덱스 만들기
    bus_road = [0] * (n + 1)
    for charger in chargers:
        bus_road[charger] = 1
 
    # 버스 운행
    # 무조건 k 만큼 가고 충전소 없으면 충전소 찾을 때까지 후진
    # 후진해서 충전소 있으면 충전하고, 거기서 다시 k 만큼 가기
    # 후진했는데 충전소 없으면 0 출력
    count = 0
    cur = 0
    move = 0
    while cur + k < n:
        if bus_road[cur + k] == 1:
            count += 1
            move = k
        else:
            for i in range(k-1, 0, -1):
                if bus_road[cur + i] == 1:
                    count += 1
                    move = i
                    break
            if move == 0:
                move = -1
 
        if move == -1:
            count = 0
            break
        else:
            cur += move
            move = 0
    print(f'#{test_case} {count}')