# https://www.acmicpc.net/problem/2661
def check(num):
    for i in range(-1, -N // 2 - 1, -1):
        pattern = num[i:]
        if num[i - len(pattern): i] == pattern:
            return False

    return True


def recur(num):
    if len(num) == N:
        print(num)
        exit()

    for s in range(1, 4):
        next_num = num + str(s)
        if check(next_num):
            recur(next_num)


N = int(input())

for i in range(1, 4):
    recur(str(i))
