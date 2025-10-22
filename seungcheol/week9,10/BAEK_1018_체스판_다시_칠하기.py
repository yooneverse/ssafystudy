def brute(sr, sc):
    black = 0
    white = 0
    for r in range(8):
        for c in range(8):
            current = chess[sr + r][sc + c]
            if (r + c) % 2:
                if current == 'B':
                    black += 1
                else:
                    white += 1
            else:
                if current == 'B':
                    white += 1
                else:
                    black += 1
    return min(black, white)

def solve():
    answer = 64

    for i in range(N - 7):
        for j in range(M - 7):
            answer = min(brute(i, j), answer)
            if not answer:
                print(0)
                return
    print(answer)

N, M = map(int, input().split())

chess = [input() for _ in range(N)]

solve()
