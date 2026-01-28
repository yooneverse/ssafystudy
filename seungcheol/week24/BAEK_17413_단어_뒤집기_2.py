import sys
input = sys.stdin.readline

sentence = input().strip()
answer = ''
tmp = ''
flag = False

for s in sentence:
    if flag:
        if s == '>':
            flag = False
        answer += s
    else:
        if s == '<':
            answer += tmp[::-1]
            tmp = ''
            flag = True
            answer += s
            continue
        elif s == ' ':
            answer += tmp[::-1]
            tmp = ''
            answer += s
            continue
        tmp += s
answer += tmp[::-1]
print(answer)
