import sys
sys.stdin = open('C:/Users/bsy40/OneDrive/Desktop/ssafystudy/suyeon/input.txt', 'r')

ICP = {'*': 2, '+': 1}
ISP = {'*': 2, '+': 1}

def Infix_to_Postfix(infix):
    postfix = ''
    stack = []
    for token in infix:
        # 피연산자
        if token not in '*+':
            postfix += token
        
        # 연산자
        elif not stack: # 스택이 비어있는 경우
            stack.append(token)
        elif ICP[token] > ISP[stack[-1]]: # 우선 순위 높음
            stack.append(token)
        else: # 우선 순위 낮음
            while stack:
                if ICP[token] <= ISP[stack[-1]]:
                    postfix += stack.pop()
                else:
                    break
            stack.append(token)
    
    if stack: # 스택에 남은 연산자가 있는 경우
        while stack:
            postfix += stack.pop()
    return postfix

def Calculate_Postfix(postfix):
    stack = []
    for token in postfix:
        # 피연산자
        if token not in '*+':
            stack.append(int(token))

        # 연산자
        elif token == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        else: # token == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
    
    return stack[0] # 무조건 연산 결과 1개만 남아야함

T = 10
for test_case in range(1, T + 1):
    infix_len = int(input())
    infix = input()

    result = Calculate_Postfix(Infix_to_Postfix(infix))
    
    print(f'#{test_case} {result}')