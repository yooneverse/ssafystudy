import sys

while True:
    line = sys.stdin.readline().rstrip()
    
    if line == '.':
        break

    stack = []
    ok = True

    for token in line:
        # (나 [면 스택에 넣기
        if token == '(' or token == '[':
            stack.append(token)

        # )나 ]면 처리하기
        elif token == ')':
            if len(stack) == 0 or stack[-1] != '(':
                ok = False
                break
            stack.pop()
        
        elif token == ']':
            if len(stack) == 0 or stack[-1] != '[':
                ok = False
                break
            stack.pop()
        
        # 영어나 공백이면 무시하기
        else:
            continue
    
    if ok and not stack:
        print('yes')
    else:
        print('no')