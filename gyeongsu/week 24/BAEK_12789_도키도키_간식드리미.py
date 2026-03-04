n = int(input())
arr = list(map(int ,input().split()))


start, end = 1, n
stack = []

for i in range(n):
    
    cur = arr[i]
        
    if arr[i] == start:
        start += 1
        while stack and stack[-1] == start:
            stack.pop()
            start += 1
    else:
        stack.append(cur)
        

if start -1 == end:
    print("Nice")
else:
    print("Sad")