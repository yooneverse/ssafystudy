
N, M = map(int, input().split()) # N: 행, M: 열


board = [input().strip() for _ in range(N)] # 공백없는 문자열 -> 보드 입력

min_count = 64  # 칸 전부가 가장 큰 값이니까 전체 칸 수로 초기 설정

# 행, 열 순회로 색깔 확인하기
for i in range(N - 7):         # 세로로 8칸씩 자를 수 있는 시작점
    for j in range(M - 7):     # 가로로 8칸씩 자를 수 있는 시작점
        count1 = 0             # 왼쪽 위가 'W'로 시작한다고 가정
        count2 = 0             # 왼쪽 위가 'B'로 시작한다고 가정

        # 8x8 범위 안을 전부 확인
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                # (x + y)가 짝수면, 시작점과 같은 색이어야 함
                # (x + y)가 홀수면, 시작점과 반대 색이어야 함

                if (x + y) % 2 == 0:  # 짝수칸
                    if board[x][y] != 'W':  # W로 시작했는데 다르면 +1
                        count1 += 1
                    if board[x][y] != 'B':  # B로 시작했는데 다르면 +1
                        count2 += 1
                else:  # 홀수칸
                    if board[x][y] != 'B':
                        count1 += 1
                    if board[x][y] != 'W':
                        count2 += 1

        # 두 경우 중 더 작은 값 선택
        result = min(count1, count2)

        # 지금까지 본 것 중 제일 작은 값 갱신
        if result < min_count:
            min_count = result

# 모든 8x8 중에서 최소 다시 칠하기 개수 출력
print(min_count)
