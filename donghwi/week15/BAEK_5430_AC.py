from sys import stdin
from collections import deque

T = int(stdin.readline())

for i in range(T):
	P = stdin.readline().rstrip()
	N = int(stdin.readline())
	X = stdin.readline().rstrip()[1:-1].split(',')
	result = ''
	rcount = 0

	if N == 0:
		X = []
	else:
		X = deque(X)	

	for j in P:
		if j == 'R':
			rcount += 1
		elif j == 'D':
			if len(X) < 1:
				result = 'error'
				break
			else :
				if rcount % 2 == 0:
					X.popleft()
				else :
					X.pop()	

	if result == 'error':
		print(result)
	else :
		if rcount % 2 == 1:
			X.reverse()
		print('['+','.join(X)+']')