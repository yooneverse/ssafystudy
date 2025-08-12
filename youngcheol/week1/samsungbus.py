T = int(input())

for test_case in range(1, T + 1):
    
    count = [0] * 5001
    n = int(input())
 
    for i in range(n):
        a, b = map(int, input().split())
    
        for idx in range(a, b + 1):
            count[idx] += 1
 
    p = int(input())  # 확인해야할 정거장 개수
    bus_stop = []
    for i in range(p):
        bus_stop.append(int(input()))
    
   
    print(f'#{test_case}', *[count[stop] for stop in bus_stop])