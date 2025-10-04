N = int(input())

jump = list(map(int, input().split()))

cnt = 0

# 현재 및 다음 출발점
start = 0
# 도착점
end = 0

# 예외 처리: 시작 == 도착
if N == 1:
    print(0)
    exit()

for i in range(N):
    # 가장 먼 다음 출발지 선정
    start = max(start, jump[i] + i)

    if i == end:
        cnt += 1
        end = start
        if end >= N - 1:
            break

if end >= N-1:
    print(cnt)
else:
    print(-1)