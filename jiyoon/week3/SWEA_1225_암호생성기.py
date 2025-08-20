# 선형 큐로 푸는 방법
# 백지에서 풀게 연습해보기

T = 10

for _ in range(1, T + 1):  # 테스트 케이스 순회
    n = int(input())  # 테스트 케이스 번호
    arr = list(map(int, input().split()))  # (1) 숫자 8개를 입력 받음

    # 큐 초기화 (넉넉히 잡음)
    q = [0] * 1000000
    front = rear = -1

    # arr 원소를 큐에 넣기
    for i in arr:
        rear += 1
        q[rear] = i

    cycle = 1  # (2) 사이클 만들어서, 사이클 내 숫자만큼 front 값 빼버리기
    while True:
        front += 1
        x = q[front] - cycle

        cycle += 1
        if cycle > 5:
            cycle = 1

        if x <= 0:
            rear += 1  # (3-1) 숫자가 감소할 때, 0보다 작아지는 경우 0으로 유지
            q[rear] = 0
            break  # (3-2) 프로그램 종료

        else:  # 0이 아니면
            rear += 1
            q[rear] = x

    # 출력 (입력받은 번호 그대로)
    print(f"#{n}", *q[rear - 7:rear + 1])


# 원형 큐로 풀어보기
T = 10

for _ in range(1, T + 1):  # 테스트 케이스 순회
    n = int(input())  # 테스트 케이스 번호
    arr = list(map(int, input().split()))  # 숫자 8개 입력

    # 원형 큐 초기화
    N = 8
    q = [0] * (N + 1)  # 편의상 크기를 하나 더 크게
    front = rear = 0

    for i in arr:
        rear = (rear + 1) % (N + 1)
        q[rear] = i

    cycle = 1  # (2) 사이클 만들어서, 사이클 내 숫자만큼 front 값 빼버리기
    while True:
        front = (front + 1) % N
        x = q[front] - cycle

        cycle += 1
        if cycle > 5:
            cycle = 1

        rear = (rear + 1) % (N + 1)
        if x <= 0:
            q[rear] = 0  # (3-1) 숫자가 감소할 때, 0보다 작아지는 경우 0으로 유지
            break  # (3-2) 프로그램 종료

        else:  # 0이 아니면
            q[rear] = x

    # 힌트: 애초에 front를 이동한다고 생각하고 중심은 고정, 인덱스가 옮겨간다고 생각해서 옮기기
    # 원형 큐니까 슬라이싱으로 잘라내기 불가
    # 그러니까 하나하나 뽑아내서 인덱스를 돌려가며 추출해서 따로 담음
    # 여기를 잘 모르겠다

    password = []
    idx = (front + 1) % (N + 1)
    for _ in range(N): # N개의 수만큼
        password.append(q[idx])
        idx = (idx + 1) % (N + 1)

    # 출력 (리스트 풀어서 출력)
    print(f"#{n}", *password)




