# BAEK 1520. 내리막 길
# DP 방식은 맞는 것 같은데 재귀 한도에 자꾸 걸려서 한도 늘림
import sys
sys.setrecursionlimit(10000)

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]

# 델타 값 설정
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

# dp 체크 2차원 배열 생성
dp = [[-1] * N for _ in range(M)]


# 길찾기 함수 정의
def find_path(x, y):
    # 만약 오른쪽 아래 끝에 도달하면 1을 반환
    if (x, y) == (N - 1, M - 1):
        return 1
    # 지나가는 중에 dp 값이 있다면 더 이상 진행하지 않고 dp값 반환하여 계산 줄임
    if dp[y][x] != -1:
        return dp[y][x]

    # 결과값 변수 설정
    result = 0

    # 델타로 상 우 하 좌 값 비교
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        # 2차원 배열에서 벗어나지 않고
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        # 이동할 곳의 값이 현재 위치 값보다 낮다면
        if matrix[ny][nx] >= matrix[y][x]:
            continue
        # 재귀 진행하여 결과값에 더함
        result += find_path(nx, ny)

    # 현재 위치에서 가능한 결과값을 dp 2차원 배열에 저장
    dp[y][x] = result
    # 결과값 반환
    return result


print(find_path(0, 0))
