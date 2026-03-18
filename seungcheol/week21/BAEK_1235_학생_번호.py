import sys
input = sys.stdin.readline

n = int(input().strip())

students = [input().strip()[::-1] for _ in range(n)]

length = len(students[0])
answer = 0

for i in range(length):
    answer += 1

    tmp = []

    for s in students:
        if s[0:i + 1] in tmp:
            break
        tmp.append(s[0:i + 1])
    else:
        break

print(answer)
