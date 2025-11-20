def delete_num(num):
    # 부른 숫자를 빙고판에서 0으로 바꾸기
    for r in range(N):
        for c in range(N):
            if board[r][c] == num:
                board[r][c] = 0


def bingo():
    cnt = 0  # 빙고 줄 개수 세기

    # 1. 행 돌기
    for r in range(N):
        zero_cnt = 0  # 한 행에 0이 몇 개인지 세기
        for c in range(N):
            if board[r][c] == 0:
                zero_cnt += 1
        if zero_cnt == 5:  # 한 줄이 모두 0이면
            cnt += 1

    # 2. 열 돌기
    for c in range(N):
        zero_cnt = 0
        for r in range(N):
            if board[r][c] == 0:
                zero_cnt += 1
        if zero_cnt == 5:
            cnt += 1

    # 3. 왼쪽 위 → 오른쪽 아래 대각선 검사
    zero_cnt = 0
    for i in range(N):
        if board[i][i] == 0:
            zero_cnt += 1
    if zero_cnt == 5:
        cnt += 1

    # 4. 오른쪽 위 → 왼쪽 아래 대각선 검사
    zero_cnt = 0
    for i in range(N):
        if board[i][N - 1 - i] == 0:
            zero_cnt += 1
    if zero_cnt == 5:
        cnt += 1

    # 빙고 줄이 3개 이상이면 True
    if cnt >= 3:
        return True
    else:
        return False


N = 5
# 빙고판
board = [list(map(int, input().split())) for _ in range(N)]

# 사회자가 부르는 숫자
nums = []
for _ in range(N):
    nums.extend(map(int, input().split()))

for i in range(len(nums)):
    delete_num(nums[i])
    if bingo():
        print(i + 1)  # 몇 번째 수에서 빙고인지 출력
        break
