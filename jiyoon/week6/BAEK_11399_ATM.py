N = int(input())
times = list(map(int, input().split()))

times.sort()                  # 작은 시간부터 정렬

total = 0                     # 최종 합
current = 0                   # 현재까지 누적된 합

for t in times:
    current += t              # 이번 사람까지 걸린 시간
    total += current          # 모든 사람 합계에 추가

print(total)
