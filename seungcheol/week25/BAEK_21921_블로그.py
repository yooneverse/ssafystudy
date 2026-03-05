import sys
input = sys.stdin.readline

n, x = map(int, input().split())

lst = list(map(int, input().split()))

answer = (0, 0)

tmp = count = 0

for i in range(n):
    if count < x:
        count += 1
        tmp += lst[i]
    else:
        tmp += lst[i] - lst[i - x]

    if answer[0] < tmp:
        answer = (tmp, 1)
    elif answer[0] == tmp:
        answer = (tmp, answer[1] + 1)

if answer[0]:
    print(answer[0])
    print(answer[1])
else:
    print('SAD')
