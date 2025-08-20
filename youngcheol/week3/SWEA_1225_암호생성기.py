from collections import deque

for T in range(1, 11):
    tc = int(input())
    arr = list(map(int, input().split()))
    q = deque(arr)

    while True:
        for i in range(1, 6):  # 1에서부터 5까지 범위로 감소
            x = q.popleft() - i
            if x <= 0:  # 만약 x가  0보다 작으면
                # x는 0이된다
                x = 0
                q.append(x)  # x를 q에 추가하고
                break  # 멈춘다
            q.append(x)  # 0보다 작은게 아니면 x를 추가한다.

        if x == 0:  # 만약 x값이 0이 되게 된다면 break 써야한다
            break

    print(f'#{tc}', *q)