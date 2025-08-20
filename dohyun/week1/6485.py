T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    A = []
    B = []
    C = []
    for i in range(N):
        a, b = map(int, input().split())    # Ai Bi 할당
        A.append(a)
        B.append(b)
    P = int(input())
    for j in range(P):
        c = int(input())    # Cj 할당
        C.append(c)
    bus_pass = []
    for j in range(P):  # P만큼 순회
        pass_cnt = 0    # 카운트 초기화
        for i in range(N):  # N만큼 순회
            if A[i] <= C[j] <= B[i]:    # Cj가 Ai와 Bi 사이의 정류장인지 확인
                pass_cnt += 1   # 카운트 + 1
        bus_pass.append(pass_cnt)   # 총 카운트를 빈 리스트에 추가

    print(f"#{test_case} {' '.join(map(str, bus_pass))}")
