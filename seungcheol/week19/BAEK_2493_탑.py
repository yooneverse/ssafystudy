import sys
input = sys.stdin.readline


N = int(input().strip())
tower = list(map(int, input().split()))

answer = [0] * N
last = []
tmp = 0
num = len(tower) - 1
while tower:
    tmp = tower.pop()
    if not last:
        last.append((tmp, num))
    elif last[-1][0] <= tmp:
        while last:
            row, col = last.pop()
            if row <= tmp:
                answer[col] = num + 1
            else:
                last.append((row, col))
                last.append((tmp, num))
                break
        else:
            last.append((tmp, num))
    else:
        last.append((tmp, num))
    num -= 1

print(*answer)
