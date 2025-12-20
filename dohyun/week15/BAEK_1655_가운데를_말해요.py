# BAEK 1655. 가운데를 말해요
import sys
sys.stdin = open('input.txt', 'r')

from heapq import heappush, heappop
input = sys.stdin.readline      # input 속도 향상

N = int(input())
median_low = []     # max-heap
median_high = []    # min-heap
out = []            # 빠른 출력을 위한 배열

for _ in range(N):
    heappush(median_low, -int(input()))
    if median_high and -median_low[0] > median_high[0]:
        num = -heappop(median_low)
        heappush(median_low, -heappop(median_high))
        heappush(median_high, num)
    if len(median_low) > len(median_high) + 1:
        num = -heappop(median_low)
        heappush(median_high, num)
    # print(-median_low[0])
    out.append(str(-median_low[0]))

sys.stdout.write('\n'.join(out))