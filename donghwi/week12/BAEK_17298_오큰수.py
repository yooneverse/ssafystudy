from sys import stdin

n = int(stdin.readline())
A = list(map(int,stdin.readline().rstrip().split()))
answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
	while stack and A[stack[-1]] < A[i]:
		answer[stack.pop()] = A[i]
	stack.append(i)

print(*answer)