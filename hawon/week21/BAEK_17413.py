import sys
input = sys.stdin.readline

txt = input().rstrip('\n')

# 스택 사용하기

# < 를 만나면 
# 1. 태그 밖에서 모아두던 단어가 있으면 : 스택을 모두 pop 해서 뒤집어 출력
# 2. 그다음부터는 태그 안이니까 상태(in_tag)를 True로 변경
# 3 '<'는 그대로 출력

# > 를 만나면
# 1. 태그가 끝났으므로 상태(in_tag)를 False로 변경
# 2. '>'는 그대로 출력

# 공백(' ')을 만나면
# 1. 스택을 모두 pop 해서 뒤집어 출력
# 2. 공백은 그대로 출력

# 일반 문자(알파벳/숫자)를 만나면
# 1. 태그 안이면 : 안 뒤집고 그대로 출력
# 2. 태그 밖이면 : 스택에 push

# 문자열이 끝나면
# 스택에 문자가 남아 있으면 : 모두 pop 해서 뒤집어 출력


stack = []
in_tag = False
# 나중에 출력할거 모아두기
ans = []


for ch in txt:

    # 1. '<'를 만나면 태그 시작
    if ch == '<':
        while stack:
            ans.append(stack.pop())
        in_tag = True
        ans.append(ch)
        continue

    # 2. '>'를 만나면 태그 끝
    if ch == '>':
        in_tag = False
        ans.append(ch)
        continue

    # 3. 태그 안이면 그대로 출력
    if in_tag:
        ans.append(ch)
    else:
        # 4. 태그 밖이면 단어는 스택에 쌓고, 공백이면 단어 비우고 공백 출력
        if ch == ' ':
            while stack:
                ans.append(stack.pop())
            ans.append(' ')
        else:
            stack.append(ch)

# 5. 문자열 끝났는데 단어가 남아있으면 마저 뒤집어서 출력
while stack:
    ans.append(stack.pop())

print(''.join(ans))