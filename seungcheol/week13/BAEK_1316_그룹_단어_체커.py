import sys
input = sys.stdin.readline

N = int(input().strip())
words = [input().strip() for _ in range(N)]

answer = 0
for word in words:
    tmp = None
    check = set()
    for w in word:
        if tmp != w:
            if tmp in check:
                break
            else:
                check.add(tmp)
                tmp = w
    else:
        if tmp not in check:
            answer += 1
print(answer)
