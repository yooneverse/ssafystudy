# 최초 풀이
N = int(input())

num = N
count = 0

while num > 1:
    num //= 3
    count += 1

grid = [[" "] * N for _ in range(N)]

def star(cnt, start):
    center = 1
    sr, sc = start
    if cnt != 1:
        for row in range(sr, sr + 3 ** cnt, 3 ** (cnt - 1)):
            for col in range(sc, sc + 3 ** cnt, 3 ** (cnt - 1)):
                if center == 5:
                    center += 1
                    continue
                star(cnt - 1, (row, col))
                center += 1
    else:
        for row in range(sr, sr + 3 ** cnt, 3 ** (cnt - 1)):
            for col in range(sc, sc + 3 ** cnt, 3 ** (cnt - 1)):
                if center == 5:
                    center += 1
                    continue
                grid[row][col] = "*"
                center += 1

star(count, (0, 0))

for i in range(N):
    answer = "".join(grid[i])
    print(answer)


# 더 좋은 풀이
N = int(input())

def star(n):
    if n == 1:
        return "*"

    pattern = []
    stars = star(n // 3)
    for p in stars:
        pattern.append(p * 3)
    for p in stars:
        pattern.append(p + " " * (n // 3) + p)
    for p in stars:
        pattern.append(p * 3)
    return pattern

grid = star(N)

for g in grid:
    print(g)