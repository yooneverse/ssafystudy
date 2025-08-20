# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기
from collections import deque
T = 10

for t in range(1, T+1):
    tc = int(input())
    data = list(map(int, input().split()))
    q = deque(data)

    while q[7] != 0:
        for i in range(1, 6):
            q[0] -= i
            q.append(q.popleft())

            if q[7] <= 0:
                q[7] = 0
                break
    print(f'#{tc}', end=' ')

    for i in range(8):
        print(f'{q[i]}', end=' ')
    print()
