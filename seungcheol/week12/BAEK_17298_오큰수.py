import sys
input = sys.stdin.readline

N = int(input())
lst = tuple(map(int, input().split()))
answer = [-1] * N
stack = []

for i in range(N):
    while stack and lst[stack[-1]] < lst[i]:
        answer[stack.pop()] = lst[i]
    stack.append(i)

print(*answer)
