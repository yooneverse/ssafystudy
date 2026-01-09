N, M = map(int, input().split())
snows = list(map(int, input().split()))

best = 0


def make_snow(pos, t, now_size):
    global best

    if t == M or pos >= N:
        if now_size > best:
            best = now_size
        return

    if pos + 1 <= N:
        next_size = now_size + snows[(pos + 1) - 1]  # a는 0-index라서 (칸번호-1)
        make_snow(pos + 1, t + 1, next_size)

    if pos + 2 <= N:
        next_size = (now_size // 2) + snows[(pos + 2) - 1]
        make_snow(pos + 2, t + 1, next_size)


make_snow(0, 0, 1)
print(best)