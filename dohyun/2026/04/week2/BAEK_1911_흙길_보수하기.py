# BAEK 1911. 흙길 보수하기
import sys
input = sys.stdin.readline

N, L = map(int, input().split())

# 물웅덩이를 받아와서 정렬
array = [list(map(int, input().split())) for _ in range(N)]
array.sort()

# 널빤지 시작 지점, 널빤지 개수 세기
start = cnt = 0
for a, b in array:
    # 시작 지점이 웅덩이 시작 위치보다 작으면 땡겨옴
    if start < a:
        start = a
    # 시작 지점이 웅덩이 끝 위치보다 작은 경우
    if start < b:
        # 만약 웅덩이 길이가 L로 나눠 떨어질 때 널빤지 개수 구하기
        if (b - start) % L == 0:
            boards = (b - start) // L
        # 그렇지 않으면 올림해서 계산
        else:
            boards = (b - start) // L + 1
        start += boards * L
        cnt += boards

print(cnt)