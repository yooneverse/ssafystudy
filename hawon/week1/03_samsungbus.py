# 삼성시의 버스 노선
T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    count_arr = [0] * 5002  # 정류장별 버스 개수 저장용 (Bi+1 때문에 +1 여유 공간)

    # 1) 시작점 +1, 끝점+1 -1 처리
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        count_arr[Ai] += 1  # 시작 정류장에서 버스 시작
        count_arr[Bi + 1] -= 1  # 끝 다음 정류장에서 버스 종료

    # 2) 누적합 계산 (이전 값 계속 더해주기)
    for i in range(1, 5001):
        count_arr[i] += count_arr[i - 1]

    # 3) 궁금한 정류장 값 읽기
    P = int(input())
    bus_c = []
    for _ in range(P):
        Cj = int(input())
        bus_c.append(Cj)

    result = []
    for c in bus_c:
        result.append(count_arr[c])  # 이미 완성된 배열에서 바로 꺼냄

    print(f'#{tc}', *result)