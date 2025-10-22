# 입력부
# 1. 철수의 빙고판 입력 (5x5)
board = [list(map(int, input().split())) for _ in range(5)]

# 2. 사회자가 부르는 숫자 목록 입력 (5x5)
call = [list(map(int, input().split())) for _ in range(5)]

# 3. 각 칸이 지워졌는지 표시할 visited (False = 아직 안 지워짐)
visited = [[False] * 5 for _ in range(5)]



# 빙고 개수를 세는 함수 정의

def check_bingo(visited):
    bingo_count = 0  # 완성된 빙고 줄 개수

    # 가로줄 검사
    for i in range(5):
        if all(visited[i]):          # 한 행이 전부 True라면
            bingo_count += 1

    # 세로줄 검사
    for j in range(5):
        if all(visited[r][j] for r in range(5)):  # 같은 열의 5칸이 전부 True면
            bingo_count += 1

    # 대각선 검사 (왼→오 / 오→왼)
    if all(visited[i][i] for i in range(5)):      # ↘ 방향 대각선
        bingo_count += 1
    if all(visited[i][4 - i] for i in range(5)):  # ↙ 방향 대각선
        bingo_count += 1

    return bingo_count


count = 0          # 지금까지 부른 숫자 개수
found = False      # 빙고가 완성되었는지 여부

for i in range(5):            # 사회자 숫자: 5행 반복
    for j in range(5):        # 각 행의 5개 숫자
        count += 1            # 호출 횟수 1 증가
        num = call[i][j]      # 지금 부른 숫자

        # 철수의 빙고판 전체를 탐색하며 일치하는 숫자 찾기
        for x in range(5):
            for y in range(5):
                if board[x][y] == num:
                    visited[x][y] = True  # 해당 칸 지움 (True로 표시)

# 출력부

        # 현재 빙고 줄 개수 확인
        if check_bingo(visited) >= 3:     # 빙고가 3줄 이상이면
            print(count)                  # 몇 번째 숫자에서 빙고인지 출력
            found = True                  # 빙고 완성 표시
            break                         # 안쪽 for문 종료

    if found:  # 빙고가 이미 완성되면 바깥 for문도 종료
        break
