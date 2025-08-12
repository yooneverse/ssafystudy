T = 10
for tc in range(1, T+1):
    # 필요 없는 값이므로 입력만 받아준다
    test = int(input())
    # 100 x 100 배열
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 각 행, 열, 대각선의 값 중 최댓값 구하기
    # 먼저 구하고 싶은 최댓값을 변수로
    max_val = 0

    # 1. 행을 순환하며 값을 구하기
    for r in range(100):
        first = 0
        for c in range(100):
            # 여기까지 하면 (0,1) (0,2) ... 첫번째 행이 나옴
            first += arr[r][c]
        if max_val < first:
            max_val = first

    # 2. 열을 순환하며 값을 구하기
    for c in range(100):
        second = 0
        for r in range(100):
            # 여기까지 하면 (1,0) (2,0) ... 첫번째 열이 나옴
            second += arr[r][c]
        if max_val < second:
            max_val = second

    # 3. 대각선 합 더하기
    # 우하향
    third = 0
    for r in range(100):
        third += arr[r][r]
    if max_val < third:
        max_val = third

    # 우상향
    fourth = 0
    for r in range(100):
        fourth += arr[r][99-r]
    if max_val < fourth:
        max_val = fourth

    print(f'#{tc} {max_val}')