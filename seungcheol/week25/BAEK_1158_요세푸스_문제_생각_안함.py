import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())

lst = deque(list(range(1, n + 1)))

answer = '<'
count = 0
while lst:
    tmp = lst.popleft()
    count += 1

    if count < k:
        lst.append(tmp)
    else:
        count = 0
        if lst:
            answer += str(tmp) + ', '
        else:
            answer += str(tmp) + '>'

print(answer)
