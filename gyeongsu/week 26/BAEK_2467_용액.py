n = int(input())
num = sorted(list(map(int, input().split())))

l = 0
r = n-1

min_abs = float('inf')
left, right = l, r

while l < r:
    hap = num[l]+ num[r]
    if abs(hap) < min_abs :
        min_abs = abs(hap)
        left = l
        right = r
    
    if hap > 0:
        r = r-1
    elif hap <0:
        l = l+1
    else:
        break

print(num[left], num[right])