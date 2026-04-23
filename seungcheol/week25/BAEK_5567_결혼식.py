import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

friends = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    friends[s].append(e)
    friends[e].append(s)

answer = set()
for f in friends[1]:
    answer.add(f)
    for r in friends[f]:
        answer.add(r)

if 1 in answer:
    answer.remove(1)
print(len(answer))
