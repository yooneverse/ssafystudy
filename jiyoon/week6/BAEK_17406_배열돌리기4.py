N, M, K = map(int, input().split())                 # 배열 크기 N, M / 연산 개수 K
board = [list(map(int, input().split())) for _ in range(N)]   # 원본 배열
ops = [tuple(map(int, input().split())) for _ in range(K)]    # 회전 연산들 (r, c, s)

answer = 10**9                                      # 최소 행 합 저장
used = [0]*K                                        # 연산 사용 여부 체크
order = [0]*K                                       # 연산 순서 저장

def rotate(temp, r, c, s):                          # (r, c, s) 기준으로 배열 회전
    r = r - 1                                       # 문제는 1-index, 파이썬은 0-index
    c = c - 1
    for layer in range(1, s+1):                     # 바깥 테두리부터 차례대로 회전
        top = r - layer
        left = c - layer
        bottom = r + layer
        right = c + layer

        save = temp[top][left]                      # 시작점 값 잠시 저장
        # 왼쪽 줄을 위에서 아래로 당김
        for i in range(top, bottom):
            temp[i][left] = temp[i+1][left]
        # 아래 줄을 왼쪽에서 오른쪽으로 당김
        for j in range(left, right):
            temp[bottom][j] = temp[bottom][j+1]
        # 오른쪽 줄을 아래에서 위로 당김
        for i in range(bottom, top, -1):
            temp[i][right] = temp[i-1][right]
        # 위쪽 줄을 오른쪽에서 왼쪽으로 당김
        for j in range(right, left+1, -1):
            temp[top][j] = temp[top][j-1]
        # 처음 저장해둔 값을 위쪽 줄의 두 번째 칸에 복구
        temp[top][left+1] = save

def min_row(temp):                                  # 배열에서 가장 작은 행 합 구하기
    m = 10**9
    for row in temp:
        s = sum(row)
        if s < m:
            m = s
    return m

def dfs(depth):                                     # 모든 연산 순서 만들기 (백트래킹)
    global answer
    if depth == K:                                  # 연산 순서를 다 정한 경우
        # 원본 배열 복사해서 temp에 저장
        temp = []
        for row in board:
            temp.append(row[:])
        # 정한 순서대로 회전 실행
        for idx in order:
            r, c, s = ops[idx]
            rotate(temp, r, c, s)
        # 완성된 배열의 최소 행 합 갱신
        answer = min(answer, min_row(temp))
        return
    
    # 아직 안 고른 연산이 있으면 하나씩 고름
    for i in range(K):
        if not used[i]:
            used[i] = 1                             # i번째 연산 선택
            order[depth] = i                        # 현재 위치에 기록
            dfs(depth+1)                            # 다음 연산 고르러 이동
            used[i] = 0                             # 원상 복구 (백트래킹)

dfs(0)                                              # 연산 순서 탐색 시작
print(answer)                                       # 최종 결과 출력
