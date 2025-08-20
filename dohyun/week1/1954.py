# 1954. 달팽이 숫자
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZhdubEaIe3HBIT9&contestProbId=AV5PobmqAPoDFAUq&probBoxId=AZiB15-a_6bHBIT9&type=PROBLEM&problemBoxTitle=0807_List2&problemBoxCnt=4
T = int(input())


# N이 홀수일 때 함수 작성
def odd_cal(n):
    # 반복을 위한 변수 생성
    k = 0
    m = 0
    # 배열이 3 x 3 이상일 때
    while n >= 3:
        # 오른쪽으로 이동하며 숫자 할당
        for a in range(1, n + 1):
            matrix[k][a + k - 1] = a + m
        # 아래로 이동하며 숫자 할당
        for a in range(1, n):
            matrix[a + k][n - 1 + k] = n + a + m
        # 왼쪽으로 이동하며 숫자 할당
        for a in range(1, n):
            matrix[n - 1 + k][n - a - 1 + k] = n + a + (n - 1) + m
        # 위로 이동하며 숫자 할당
        for a in range(1, n - 1):
            matrix[n - a - 1 + k][k] = n + a + 2 * (n - 1) + m
        # 외부 라인 완료 후 내부 라인 작성을 위해 변수 재할당
        m = int(8 * (n - 1) / 2)
        n -= 2
        k += 1


# N이 짝수일 때 함수 작성
def even_cal(n):
    k = 0
    m = 0
    # 배열이 2 x 2 이상일 때
    while n >= 2:
        for a in range(1, n + 1):
            matrix[k][a + k - 1] = a + m
        for a in range(1, n):
            matrix[a + k][n - 1 + k] = n + a + m
        for a in range(1, n):
            matrix[n - 1 + k][n - a - 1 + k] = n + a + (n - 1) + m
        for a in range(1, n - 1):
            matrix[n - a - 1 + k][k] = n + a + 2 * (n - 1) + m
        m = int(8 * n / 2 - 4)
        n -= 2
        k += 1


for tc in range(1, T+1):
    N = int(input())
    # N x N 배열 생
    matrix = [[0] * N for _ in range(N)]

    # N이 홀수일 때
    if N % 2 == 1:
        # 가운데 값 할당
        matrix[int((N - 1) / 2)][int((N - 1) / 2)] = N ** 2
        # 홀수 함수 호출
        odd_cal(N)

    # N이 짝수일 때
    if N % 2 == 0:
        # 짝수 함수 호
        even_cal(N)

    print(f'#{tc}')
    for result in matrix:
        print(' '.join(map(str, result)))
