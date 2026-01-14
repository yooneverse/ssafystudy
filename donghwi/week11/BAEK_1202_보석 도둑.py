# https://www.acmicpc.net/problem/1202
import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

# 보석: (무게 m, 가치 v)
gems = []
for _ in range(n):
    m, v = map(int, input().split())
    gems.append((m, v))
# 무게 오름차순 정렬
gems.sort(key=lambda x: x[0])

# 가방 용량
bags = [int(input()) for _ in range(k)]
# 용량 오름차순 정렬
bags.sort()

total = 0
idx = 0
# heapq는 최소힙이라 "가치 최대"를 꺼내기 위해 음수로 넣어 최대힙처럼 사용
max_heap = []  # 값에 -v를 넣어 사용

for cap in bags:
    # 현재 가방(cap)에 들어갈 수 있는 모든 보석을 힙에 넣기
    while idx < n and gems[idx][0] <= cap:
        m, v = gems[idx]
        heapq.heappush(max_heap, (-v, m))  # (음수 가치, 무게)
        idx += 1

    # 가장 가치가 큰 보석 하나를 꺼내서 담기
    if max_heap:
        v = -heapq.heappop(max_heap)[0]
        total += v

print(total)
