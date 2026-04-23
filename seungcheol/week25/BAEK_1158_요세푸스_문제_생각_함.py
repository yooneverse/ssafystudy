import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst = list(range(1, n + 1))
answer = []
idx = 0
while lst:
    idx = (idx + k - 1) % len(lst)
    answer.append(lst.pop(idx))

print('<' + ', '.join(map(str, answer)) + '>')
