str = input()

stack = []
res = []
tag = False    # 태그 안 존재 여부

for ch in str:
    # 시작 태그 만나면 쌓아둔 단어 뒤집어서 res에 추가함
    if ch == '<':
        while stack:
            res.append(stack.pop())
        tag = True
        res.append(ch)
    
    # 종료 태그 만나면?
    elif ch == '>':
        tag = False
        res.append(ch)
    
    # 태그 안에 있으면?
    elif tag:
        res.append(ch)
    
    # 태그 밖에 있으면?
    else:
        # 공백 만나면 단어 끝났다는 소리
        if ch == ' ':
            while stack:
                res.append(stack.pop())
            res.append(' ')
        else:
            stack.append(ch)

# 남은 단어 처리
while stack:
    res.append(stack.pop())

print(''.join(res))
