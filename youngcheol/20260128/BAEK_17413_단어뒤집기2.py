# 알파벳, 숫자 < >로 구성
# < > 안에 들어간 문자열은 뒤집지 말고 
# 나머지는 다 뒤집는다.


S = input()

stack = []
# 결과 저장 
result = []
in_tag = False

for i in S:
    if i == '<':
        # <을 만나게 되면 stack에 있는 말 다 뒤집기
        while stack:
            print(stack.pop(), end='')

        # < > 안에 있는 말은 어떻게 해야할지 몰라서 제미나이 도움 받음
        in_tag = True
        print(i, end ='')

    # >이면 그대로 출력
    elif i == '>':
        in_tag = False
        print(i, end='')
    
    # 태그 안에 있는 문자열 그대로 출력
    elif in_tag:
        print(i, end ='')
        
    else:
        if i == ' ':
            while stack:

                print(stack.pop(), end='')
            print(' ', end='')
        else:
            stack.append(i)

while stack:
    print(stack.pop(), end = '')


