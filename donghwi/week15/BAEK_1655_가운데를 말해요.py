from sys import stdin
import heapq

n = int(stdin.readline())
leftheap = []
rightheap = []
for _ in range(n):
	x = int(stdin.readline())
	if len(leftheap) == len(rightheap):
		heapq.heappush(leftheap,-x)
	else:
		heapq.heappush(rightheap,x)

	if rightheap and rightheap[0] < -leftheap[0]:
		leftvalue = heapq.heappop(leftheap)
		rightvalue = heapq.heappop(rightheap)

		heapq.heappush(leftheap,-rightvalue)
		heapq.heappush(rightheap,-leftvalue)
	print(-leftheap[0])