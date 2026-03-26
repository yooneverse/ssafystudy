import sys
input = sys.stdin.readline

n = int(input().strip())
tree = list(map(int, input().split()))
grow = list(map(int, input().split()))

match = []
for i in range(n):
    match.append((grow[i], tree[i]))

match.sort()

answer = 0
for i in range(n):
    answer += match[i][1] + match[i][0] * i

print(answer)
