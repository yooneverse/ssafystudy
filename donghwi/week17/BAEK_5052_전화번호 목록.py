from sys import stdin

t = int(input())
while t:
	n = int(stdin.readline())
	calList = [stdin.readline().rstrip() for _ in range(n)]
	calList.sort()
    
	for idx in range(len(calList)-1):
		if calList[idx] in calList[idx+1][:len(calList[idx])]:
			print("NO")
			break
	else:
		print("YES")
	t -= 1