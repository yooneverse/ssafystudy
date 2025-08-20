T = 10
for tc in range(1, T+1):
    t = input()
    arr = list(map(int, input().split()))
    N = 8
    # 현재 q [9550, 9556, 9550, 9553, 9558, 9551, 9551, 9551]

    # 원형 큐 만들기
    q = [0] * (N+1)
    front = rear = 0

    # 내가 원하는 답 > 8자리 숫자 값
    answer = []
    # 사이클마다 5번씩 빼는 과정을 거쳐야 함
    S = 5

    for i in arr:
        rear = (rear+1) % (N+1)
        q[rear] = i


    # 몇 번 반복해야되는지 모르니까 while 쓰기
    # 종료조건 : q 안의 원소가 0이 될때까지
    password = False
    while not password:
        # 돌때마다 1씩 증가한 숫자들을 빼줘야 함
        # 처음 뒤로 갈 땐 -1 그다음엔 -2 그다음엔 -3
        for s in range(1, S+1):
            # 맨 앞 원소 꺼내기
            front = (front+1) % (N+1)
            x = q[front]

            # 꺼낸거 빼기
            x -= s

            # 꺼낸 거 뒤에 넣기
            rear = (rear+1) % (N+1)
            # 만약에 꺼낸게 0보다 작거나 같으면 종료시킨다
            if x <= 0:
                q[rear] = 0
                password = True
                break
            # 아니면 맨 끝에 x를 보낸다
            else:
                q[rear] = x

    idx = (front+1) % (N+1)
    # 원소 8개만 뽑을 거니까 8번 반복
    for _ in range(N):
        answer.append(q[idx])
        # 1번 반복하면 인덱스를 늘려줘야 함
        idx = (idx +1) % (N+1)

    print(f'#{tc}', *answer)