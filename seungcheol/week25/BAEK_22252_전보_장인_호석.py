import sys

input = sys.stdin.readline

from heapq import heappop, heappush

q = int(input().strip())

answer = 0

gorila = {}

for _ in range(q):
    tmp_lst = list(input().split())
    length = len(tmp_lst)

    if tmp_lst[0] == "1":
        if tmp_lst[1] not in gorila:
            gorila[tmp_lst[1]] = []
        for i in range(3, length):
            heappush(gorila[tmp_lst[1]], -int(tmp_lst[i]))
    else:
        if tmp_lst[1] not in gorila:
            continue
        sensor = 0
        while gorila[tmp_lst[1]]:
            if sensor == int(tmp_lst[2]):
                break
            answer += -heappop(gorila[tmp_lst[1]])
            sensor += 1

print(answer)
