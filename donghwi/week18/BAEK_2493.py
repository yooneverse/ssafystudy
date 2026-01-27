from sys import stdin

N = int(stdin.readline())

razor = list(map(int,stdin.readline().split(' ')))
stack = []
result = []

for i in range(N):
	while stack:
		if stack[-1][1] > razor[i]:
			result.append(stack[-1][0] + 1)
			break
		else:
			stack.pop()
	if not stack:
		result.append(0)
	stack.append([i,razor[i]])

print(' '.join(map(str,result)))