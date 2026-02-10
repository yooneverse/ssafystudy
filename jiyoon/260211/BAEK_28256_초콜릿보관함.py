from collections import deque

# 테스트 케이스 개수 입력
T = int(input())

# 상, 하, 좌, 우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    # 3x3 초콜릿 보관함 입력
    board = [list(input()) for _ in range(3)]

    # 숫자 화면에 표시된 정보 입력
    data = list(map(int, input().split()))
    n = data[0]          # 표시된 숫자의 개수
    expected = data[1:] # 표시된 숫자 리스트

    # 방문 여부 체크 배열 (3x3)
    visited = [[False] * 3 for _ in range(3)]

    # 실제로 계산한 연결 요소 크기들을 저장할 리스트
    actual = []

    # 모든 칸을 순회
    for i in range(3):
        for j in range(3):
            # 초콜릿이 있고, 아직 방문하지 않았다면
            if board[i][j] == 'O' and not visited[i][j]:
                # BFS 시작
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True

                # 현재 연결 요소의 크기
                count = 1

                while queue:
                    x, y = queue.popleft()

                    # 상하좌우 탐색
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        # 격자 범위 안에 있고
                        if 0 <= nx < 3 and 0 <= ny < 3:
                            # 초콜릿이 있으며 아직 방문 안 했으면
                            if board[nx][ny] == 'O' and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                count += 1  # 연결 요소 크기 증가

                # 하나의 연결 요소 탐색이 끝났으므로 결과 저장
                actual.append(count)

    # 실제 연결 요소 크기들을 오름차순 정렬
    actual.sort()

    # 입력으로 주어진 숫자들도 이미 오름차순이지만 안전하게 정렬
    expected.sort()

    # 두 리스트가 완전히 같으면 1, 아니면 0 출력
    if actual == expected:
        print(1)
    else:
        print(0)
