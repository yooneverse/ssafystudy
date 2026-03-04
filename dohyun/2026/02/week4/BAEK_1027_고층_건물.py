# BAEK 1027. 고층 건물
import sys
input = sys.stdin.readline

N = int(input())
height = list(map(int, input().split()))

result = 0

# N 개의 건물 모두 탐색(Brute Force)
for i in range(N):
    count = 0   # 보이는 건물의 개수
    max_dy, max_dx = -1, 0  # 초기 기울기를 음의 무한대로 설정

    # 나눗셈은 오차가 발생할 수 있으므로 교차 곱셈 사용
    # 왼쪽부터 계산하는데, 최대 기울기 갱신을 통해 보이는 건물 개수 계산
    # dx = i - j로 둬서 오른쪽에 있는 것처럼 생각함
    for j in range(i-1, -1, -1):
        dy = height[j] - height[i]
        dx = i - j
        if dx * max_dy < dy * max_dx:
            max_dy, max_dx = dy, dx
            count += 1

    # 오른쪽은 dx = k - i로 두며 그대로 진행
    max_dy, max_dx = -1, 0
    for k in range(i+1, N):
        dy = height[k] - height[i]
        dx = k - i
        if dx * max_dy < dy * max_dx:
            max_dy, max_dx = dy, dx
            count += 1

    if result < count:
        result = count

print(result)
