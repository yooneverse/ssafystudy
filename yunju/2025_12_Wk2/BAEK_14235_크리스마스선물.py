'''
썰매 크기 제한
세계 거점. 선물 충전
가진 선물 중 최대 가치 선물 하나 줌

아이들 거점 정보 선물 가치
줄 선물 없다면 -1

입력
아이들과 거점지를 방문한 횟수 n

아래 n개의 줄
0 : 아이들 만남
2 3 2 : 거점지에서 2개의 선물 충전. 가치는 3, 2
'''

'''
최댓값 하나만 나오면 됨 >> heap
'''

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
presents = []

for _ in range(n):
    numbers = list(map(int, input().split()))
    if numbers[0] == 0:
        if presents:
            print(-heappop(presents))
        else:
            print(-1)
    else:
        for p in numbers[1:]:
            heappush(presents,-p)



