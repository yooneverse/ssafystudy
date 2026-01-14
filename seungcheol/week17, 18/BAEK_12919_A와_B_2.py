import sys

input = sys.stdin.readline

def check(start):
    global answer

    length = len(start)

    if length < goal_length:
        return

    if start == S:
        answer = 1
        return

    if start[length - 1] == 'A':
        check(start[:length - 1])
        if answer:
            return

    if start[0] == 'B':
        tmp = start[1:]
        check(tmp[::-1])
        if answer:
            return
    return

S = input().strip()

T = input().strip()

answer = 0

goal_length = len(S)
check(T)

print(answer)
