import sys
input = sys.stdin.readline

def dfs(d, tmp):
    global answer
    if d:
        answer = min(answer, d + abs(tmp - goal))
    if d == size + 1:
        return
    for c in range(10):
        if c in broken:
            continue
        dfs(d + 1, tmp + c * (10 ** d))

N = list(map(int, input().strip()))
size = len(N)
goal = 0
for i in range(size - 1, -1, -1):
    goal += N[size - 1 - i] * (10 ** i)
M = int(input())

broken = ()
if M:
    broken = set(map(int, input().split()))

answer = abs(goal - 100)
flag = True

if M != 10:
    for i in range(size):
        if N[i] in broken:
            break
    else:
        answer = min(size, answer)
        flag = False
    if flag:
        dfs(0, 0)

print(answer)
