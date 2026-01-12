import sys
input = sys.stdin.readline

from heapq import heappush, heappop

N = int(input().strip())

front = []
back = []
mid = int(input().strip())

print(mid)

for i in range(N - 1):
    num = int(input().strip())
    if num < mid:
        heappush(front, -num)
        if i % 2 == 0:
            heappush(back, mid)
            mid = -heappop(front)

    else:
        heappush(back, num)
        if i % 2:
            heappush(front, -mid)
            mid = heappop(back)

    print(mid)
