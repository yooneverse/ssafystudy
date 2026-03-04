from sys import stdin

N = list(map(int,stdin.readline().split()))
arr = [i for i in range(1,N[0]+1)]

result = []
num = 0
for i in range(N[0]):
	num += N[1]-1
	if num >= len(arr):
		num = num%len(arr)

	result.append((str(arr.pop(num))))
print('<'+ ', '.join((result)) + '>')