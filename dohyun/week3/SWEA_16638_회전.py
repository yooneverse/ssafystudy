# 16638. 6일차 - 회전
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    natural = list(map(int, input().split()))
    cq = [0] * (N + 1)
    front = rear = 0

    for i in natural:
        rear = (rear + 1) % (N + 1)
        cq[rear] = i

    for j in range(M):
        front = (front + 1) % (N + 1)
        rear = (rear + 1) % (N + 1)
        cq[rear] = cq[front]

    print(f'#{tc} {cq[(front + 1) % (N + 1)] }')
