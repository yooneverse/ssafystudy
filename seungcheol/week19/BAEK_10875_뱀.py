import sys
input = sys.stdin.readline

L = int(input().strip())
N = int(input().strip())

point = [L, L]
horizon = []
horizon.append((L, L, L))

vertical = []
vertical.append((L, L, L))

direction = 0

# 
flag = False

answer = 0

for x in range(N + 1):
    if x == N:
        t = 200000002
    else:
        t, d = input().split()
        t = int(t)
    tmp = 200000002

    # 오른쪽(c++)
    if direction == 0:
        for c, rs, re in vertical:
            # 수평선의 y가 수직선의 y 범위에 포함됨
            # 수평선의 x 범위에 수직선의 x가 포함됨
            if rs <= point[0] <= re and point[1] + 1 <= c <= point[1] + t:
                flag = True
                tmp = min(tmp, c - point[1])
        else:
            if flag:
                answer += tmp
                break
            if point[1] + t >= 2 * L + 1:
                answer += 2 * L + 1 - point[1]
                break
            horizon.append((point[0], point[1], point[1] + t))
            point[1] += t
            answer += t
    # 위(r--)
    elif direction == 1:
        for r, cs, ce in horizon:
            # 수직선의 x가 수평선의 x 범위에 포함됨
            # 수직선의 y 범위에 수평선의 y가 포함됨
            if cs <= point[1] <= ce and point[0] - t <= r <= point[0] - 1:
                flag = True
                tmp = min(tmp, point[0] - r)
        else:
            if flag:
                answer += tmp
                break
            if point[0] - t < 0:
                answer += point[0] + 1
                break
            vertical.append((point[1], point[0] - t, point[0]))
            point[0] -= t
            answer += t

    # 왼쪽(c--)
    elif direction == 2:
        for c, rs, re in vertical:
            # 수평선의 y가 수직선의 y 범위에 포함됨
            # 수평선의 x 범위에 수직선의 x가 포함됨
            if rs <= point[0] <= re and point[1] - t <= c <= point[1] - 1:
                flag = True
                tmp = min(tmp, point[1] - c)
        else:
            if flag:
                answer += tmp
                break
            if point[1] - t < 0:
                answer += point[1] + 1
                break
            horizon.append((point[0], point[1] - t, point[1]))
            point[1] -= t
            answer += t

    # 아래(r++)
    else:
        for r, cs, ce in horizon:
            # 수직선의 x가 수평선의 x 범위에 포함됨
            # 수직선의 y 범위에 수평선의 y가 포함됨
            if cs <= point[1] <= ce and point[0] + 1 <= r <= point[0] + t:
                flag = True
                tmp = min(tmp, r - point[0])
        else:
            if flag:
                answer += tmp
                break
            if point[0] + t >= 2 * L + 1:
                answer += 2 * L + 1 - point[0]
                break
            vertical.append((point[1], point[0], point[0] + t))
            point[0] += t
            answer += t

    if d == 'L':
        direction = (direction + 1) % 4
    elif d == 'R':
        direction = (direction + 3) % 4

print(answer)
