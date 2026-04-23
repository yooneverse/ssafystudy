import sys
input = sys.stdin.readline

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

T = int(input().strip())

for _ in range(T):
    command = input().strip()

    turtle = [0, 0]

    left = right = top = bottom = D = 0

    for C in command:
        if C == "F":
            turtle[0] += delta[D][0]
            turtle[1] += delta[D][1]

        elif C == "B":
            turtle[0] -= delta[D][0]
            turtle[1] -= delta[D][1]
        elif C == "L":
            D = (D + 3) % 4
            continue
        else:
            D = (D + 1) % 4
            continue

        bottom = min(bottom, turtle[0])
        top = max(top, turtle[0])
        left = min(left, turtle[1])
        right = max(right, turtle[1])

    answer = (top - bottom) * (right - left)
    print(answer)
