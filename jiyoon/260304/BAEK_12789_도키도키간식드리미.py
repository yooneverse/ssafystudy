import sys
input = sys.stdin.readline

N = int(input().strip())                 # 학생 수 N
line = list(map(int, input().split()))   # 현재 줄(앞 -> 뒤) 순서

stack = []                               # 옆 대기 공간(스택)
need = 1                                 # 지금 간식 받아야 하는 번호

for x in line:                           # 줄을 앞에서부터 한 명씩 처리
    while stack and stack[-1] == need:   # 스택 맨 위가 필요 번호면 계속 꺼내기
        stack.pop()                      # 스택에서 나오기
        need += 1                        # 다음 번호로 진행

    if x == need:                        # 지금 줄 맨 앞 사람이 필요 번호면
        need += 1                        # 바로 간식 받고 다음 번호로
    else:                                # 아니면
        stack.append(x)                  # 옆 대기 공간(스택)에 세워두기

while stack and stack[-1] == need:       # 줄 처리가 끝난 뒤에도 스택에서 꺼낼 수 있으면 꺼내기
    stack.pop()                          # 스택에서 나오기
    need += 1                            # 다음 번호로

print("Nice" if need == N + 1 else "Sad")# 전부 1..N 처리했으면 Nice, 아니면 Sad