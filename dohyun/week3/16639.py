# 16639. 6일차 - 피자굽기
from collections import deque
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    deq = deque()
    deq_idx = deque()
    cnt = 0

    for i in range(N):
        deq.append(pizza[i])
        deq_idx.append(i)
        cnt += 1

    while len(deq) > 1:
        if deq[0] // 2 != 0:
            deq.append(deq.popleft() // 2)
            deq_idx.append(deq_idx.popleft())
        elif deq[0] // 2 == 0:
            deq.popleft()
            deq_idx.popleft()
            if cnt < M:
                deq.append(pizza[cnt])
                deq_idx.append(cnt)
                cnt += 1

    print(f'#{tc} {deq_idx.pop() + 1}')
