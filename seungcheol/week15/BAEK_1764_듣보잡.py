import sys
input = sys.stdin.readline

N, M = map(int, input().split())

store = {}
for _ in range(N):
    no_listen = input().strip()
    store[no_listen] = True

answer = 0
names = []
for _ in range(M):
    no_look = input().strip()
    if store.get(no_look, False):
        answer += 1
        names.append(no_look)

names.sort()

print(answer)
for name in names:
    print(name)
