n, k = map(int, input().split())
arr = list(map(int, input().split()))



hap = 0
left = 0
short = n
if sum(arr) < k:
    short = 0
for i in range(n):
    hap += arr[i]
    while hap >= k:
        short = min(short, i -left + 1)
        hap -= arr[left]
        left += 1

    
print(short)
