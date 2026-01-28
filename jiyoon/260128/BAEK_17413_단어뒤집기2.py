import sys

line = sys.stdin.readline()   # 입력 문자열

out = []     # 결과를 하나씩 담아서 마지막에 join
word = []    # 단어를 뒤집기 위해 임시로 쌓아두는 공간
pos = 0      # 문자열에서 현재 보고 있는 위치

while pos < len(line):
    # 입력 끝의 개행 문자는 문제 조건에 필요 없어서 여기서 종료
    if line[pos] == '\n':
        break

    # 태그 시작을 만난 경우
    if line[pos] == '<':
        # 태그 앞에 단어가 있으면 먼저 뒤집어서 출력해야 함
        while word:
            out.append(word.pop())

        # '<'부터 '>'까지는 뒤집지 않고 그대로 출력
        while line[pos] != '>':
            out.append(line[pos])
            pos += 1

        # '>' 문자도 결과에 포함
        out.append('>')

    # 공백을 만난 경우
    elif line[pos] == ' ':
        # 공백 전까지가 하나의 단어이므로 스택에 쌓인 문자 처리
        while word:
            out.append(word.pop())

        # 공백 자체는 그대로 출력
        out.append(' ')

    # 일반 문자(태그도 아니고 공백도 아닌 경우)
    else:
        # 단어의 일부이므로 일단 모아둠
        word.append(line[pos])

    # 다음 문자로 이동
    pos += 1

# 문자열이 끝났을 때 아직 처리하지 못한 단어가 남아 있을 수 있음
while word:
    out.append(word.pop())

print(''.join(out))
