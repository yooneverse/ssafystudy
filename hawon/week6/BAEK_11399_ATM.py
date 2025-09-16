# 입력
N = int(input())
P = list(map(int, input().split()))

# 1. 인출 시간을 오름차순으로 정렬
P.sort()

# 2. 누적합 계산
total = 0       # 최종 출력값
current = 0     # 현재까지의 누적 대기 시간

for time in P:
    current += time
    total += current

print(total)
