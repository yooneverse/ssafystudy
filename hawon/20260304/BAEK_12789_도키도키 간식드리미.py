'''
BAEK_12789_도키도키 간식드리미
원래 줄: 학생들이 서 있음 (앞에서부터 한 명씩만 볼 수 있음)
옆 공간(스택): 잠깐 빼두는 곳 (위에 있는 것만 꺼낼 수 있음)
목표: 1, 2, 3, ... N 순서대로 내보내기
'''

import sys
input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))

stack = []
need = 1

for x in line:
    # 보조 줄에서 꺼낼 수 있으면 먼저 꺼내기
    while stack and stack[-1] == need:
        stack.pop()
        need += 1

    if x == need:
        need += 1
    else:
        stack.append(x)

# 마지막으로 보조 줄에서 남은 것 처리
while stack and stack[-1] == need:
    stack.pop()
    need += 1

print("Nice" if need == N + 1 else "Sad")