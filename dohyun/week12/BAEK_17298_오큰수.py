# BAEK 17298. 오큰수
# 스택 사용
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))

stack = []  # stack 사용
ans = [0] * N   # 정답 배열
# N 번 반복(위치 인덱스)
for i in range(N):
    # 스택이 비어있으면 인덱스 그대로 추가
    if not stack:
        stack.append(i)
    else:
        s = stack[-1]   # 간소화를 위한 변수
        # 스택의 인덱스 숫자를 정답 배열의 인덱스로 사용하면서
        # 정답 배열에 더 큰 숫자를 치환
        if A[s] < A[i]:
            # 스택이 남아있고
            # 스택 끝자리 인덱스의 숫자가 현재 인덱스의 숫자보다 작으면 반복
            while stack and A[s] < A[i]:
                ans[s] = A[i]
                # 그 다음(먼저 들어온) 스택 비교를 위해 pop()
                stack.pop()
                # 변수 조정
                s = stack[-1]
            # 반복 끝나면 다음 비교를 위해 스택에 i 추가
            stack.append(i)
        # 앞 자릿수가 더 크면 그대로 스택에 추가
        else:
            stack.append(i)

# 비교가 끝내고 스택이 남아있다면
# 오큰수가 없다는 의미
# 정답 배열의 인덱스 자리에 전부 -1 추가
if stack:
    for k in range(len(stack)):
        ans[stack[k]] = -1
    stack = []

print(*ans)
