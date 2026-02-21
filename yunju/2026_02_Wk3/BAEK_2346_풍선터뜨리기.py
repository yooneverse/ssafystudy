import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

deq = deque(enumerate(map(int, input().split())))
answer =[]


while deq:
    idx, now_turn = deq.popleft()
    answer.append(idx+1)

    if now_turn > 0 :
        deq.rotate(-(now_turn-1))
    elif now_turn < 0:
        deq.rotate(-now_turn)
print(*answer)