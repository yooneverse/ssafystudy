T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 카운팅 배열 생성, 입력 조건에 맞춰 최대로 만듦
    # 다른 코드에선 이렇게 만드는 것을 지양하는게 좋을 것 같습니다.
    count = [0] * 5001
    n = int(input())
 
    for i in range(n):
        num_a, num_b = map(int, input().split())
        # a, b 받자마자 버스가 다니는 정거장을 count 배열에 모두 표시
        for idx in range(num_a, num_b + 1):
            count[idx] += 1
 
    p = int(input())  # 확인해야할 정거장 개수
    bus_stop = [] # 출력에서 바로 정거장을 찾기 위해 리스트를 만들었습니다.
    for i in range(p):
        bus_stop.append(int(input()))
    
    # count 배열에서 입력된 정거장 인덱스를 찾고, 해당 인덱스에 저장된 지나가는 버스 노선 수 출력
    print(f'#{test_case}', *[count[stop] for stop in bus_stop])