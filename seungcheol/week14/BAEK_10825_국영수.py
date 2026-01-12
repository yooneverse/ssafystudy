import sys
input = sys.stdin.readline

from heapq import heappop, heappush

N = int(input().strip())
pq = []
for _ in range(N):
    name, kor, eng, math = input().split()
    heappush(pq, (-int(kor), int(eng), -int(math), name))

for _ in range(N):
    answer = heappop(pq)
    print(answer[3])
