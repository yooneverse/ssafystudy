import sys
input = sys.stdin.readline

h, w = map(int, input().split())

wall = list(map(int, input().split()))

answer = 0

low = 501
left = (501, 501)

for i in range(w):
    tmp = wall[i]
    # 왼쪽 기둥을 찾기 전(현재 높이 0)
    if not tmp and left[0] == 501:
        continue
    # 왼쪽 기둥
    elif tmp and left[0] == 501:
        left = (tmp, i)
    # 구덩이
    elif tmp < left[0] and tmp <= low:
        low = min(low, tmp)
    # 왼쪽 기둥 이동
    elif tmp >= left[0] and low == 501:
        left = (tmp, i)
    # 오른쪽 기둥
    # 두 기둥 사이는 수몰
    # 오른쪽 기둥이 왼쪽 기둥이 됨
    elif tmp >= left[0] and low != 501:
        line = min(left[0], tmp)
        for j in range(left[1] + 1, i):
            answer += line - wall[j]
            wall[j] = line
        left = (tmp, i)
        low = 501
    # 왼쪽 기둥보다는 낮지만 작은 구덩이를 만들수 있는 높이
    elif tmp > low:
        for j in range(left[1] + 1, i):
            if wall[j] < tmp:
                answer += tmp - wall[j]
                wall[j] = tmp
        low = tmp
print(answer)
