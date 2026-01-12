def dfs(r, c):
    global answer

    num = grid[r][c]

    if not num:
        return

    if answer:
        return

    if r == c == N - 1:
        answer = True
        return

    if r + num < N:
        dfs(r + num, c)
    if c + num < N:
        dfs(r, c + num)

N = int(input())
grid = [tuple(map(int, input().split())) for _ in range(N)]
answer = False

dfs(0, 0)

if answer:
    print('HaruHaru')
else:
    print('Hing')
