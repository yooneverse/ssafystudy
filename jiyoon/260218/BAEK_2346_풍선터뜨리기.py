import sys
input = sys.stdin.readline

n = int(input())
moves = list(map(int, input().split()))

# (풍선번호, 이동값)
balloons = [(i + 1, moves[i]) for i in range(n)]

result = []
idx = 0  # 현재 위치

while balloons:
    # 1. 현재 풍선 제거
    num, move = balloons.pop(idx)
    result.append(num)

    if not balloons:  # 마지막이면 종료
        break

    # 2. 이동값에 따라 인덱스 이동
    if move > 0:
        # 오른쪽 이동
        idx = (idx + move - 1) % len(balloons)
    else:
        # 왼쪽 이동
        idx = (idx + move) % len(balloons)

print(*result)