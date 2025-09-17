# BAEK 11060. 점프 점프
# 1) 선형 큐 버전
def maze_q():
    q = [0]     # 큐 생성
    # 큐에 원소가 있는 동안 반복
    while q:
        # 선입선출
        x = q.pop(0)

        # 만약 점프가 끝에 다다랐으면 방문값(점프 횟수) 반환
        if x == N - 1:
            return visited[x]

        # A 배열 값의 범위만큼 점프
        for i in range(1, A[x] + 1):
            # 점프한 값이 N을 넘지 않고, 점프할 곳을 방문한 적이 없다면
            # 큐에 추가 후 방문 배열에 점프 횟수 기록
            if x + i < N and visited[x + i] == 0:
                q.append(x + i)
                visited[x + i] = visited[x] + 1
    # 반환값 없이 반복문 종료시 -1 반환
    return -1


# 방문 배열 생성
visited = [0] * N


# 2) 원형 큐 버전
def maze_cq():
    # 시작점이 도착점이면 점프 횟수 0 반환
    if N == 1:
        return 0
    # 시작점에서 갈 수 있는 곳이 없으면 -1 반환
    if A[0] == 0:
        return -1

    # 원형 큐 생성
    q = [0] * (N + 1)
    front = rear = 0

    # 큐가 비었으면 True, 아니면 False 반환
    def empty():
        return front == rear

    # 큐가 꽉 찼으면 True, 아니면 False 반환
    def full():
        return (rear + 1) % (N + 1) == front

    # 큐가 꽉 찼다면 enqueue
    def enq(x):
        nonlocal rear
        if full():
            return False
        rear = (rear + 1) % (N + 1)
        q[rear] = x
        return True

    # 큐가 비어있지 않다면 dequeue
    def deq():
        nonlocal front
        if empty():
            return None
        front = (front + 1) % (N + 1)
        return q[front]

    # 점프 횟수 기록할 배열 생성
    jump = [0] * N
    # 시작점 enqueue
    enq(0)

    # 만약 큐가 비어있지 않다면 반복
    while not empty():
        # 현재 위치로 dequeue 값 설정
        idx = deq()
        # 이동 가능한 거리 설정
        step = A[idx]

        # 현재 위치에서 이동 가능한 거리를 더한 범위에서 반복
        for i in range(idx + 1, idx + step + 1):
            # 이동 거리가 N을 넘어설 때 반복 중단
            if i == N:
                break
            # 만약 i 에 방문한 적이 있다면 넘어감
            if jump[i] != 0:
                continue
            # 다음에 이동할 위치로 점프한 횟수 기록
            # 이전까지 점프한 횟수에 1 추가
            jump[i] = jump[idx] + 1
            # 도착점에 다다랐으면 점프 횟수 반환
            if i == N - 1:
                return jump[i]
            # 큐에 다음 위치 저장
            enq(i)
    # 반환값 없이 반복문 종료시 -1 반환
    return -1


N = int(input())
A = list(map(int, input().split()))

print(maze_cq())
print(maze_q())
