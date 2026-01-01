import sys
input = sys.stdin.readline


def find(start,end):
    global ans
    cnt = 0
    mid = (start+end)//2
    if start > end:
        return

    for num in lines:
        cnt += num//mid

    if cnt >= N:
        ans = max(ans, mid)
        find(mid+1,end)

    else:
        find(start, mid-1)



K, N = map(int, input().split())
lines = []
for i in range(K):
    l = int(input())
    lines.append(l)
average = sum(lines)//N

ans = 0
find(1,average)
print(ans)
