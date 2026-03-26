import sys
input = sys.stdin.readline

n = int(input().strip())
lst = list(map(int, input().split()))

stack = []
idx = 0
answer = 1
while idx < n:
    if lst[idx] == answer:
        idx += 1
        answer += 1
    elif stack and stack[-1] == answer:
        stack.pop()
        answer += 1
    else:
        stack.append(lst[idx])
        idx += 1

while stack:
    if stack[-1] == answer:
        stack.pop()
        answer += 1
    else:
        print("Sad")
        break
else:
    print("Nice")
