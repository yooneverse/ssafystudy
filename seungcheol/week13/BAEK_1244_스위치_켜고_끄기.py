import sys
input = sys.stdin.readline

def check(i, d):
    return 0 <= i - d < s_n and 0 <= i + d < s_n

s_n = int(input().strip())
switch = list(map(int, input().split()))
st_n = int(input().strip())
student = [tuple(map(int, input().split())) for _ in range(st_n)]

for gender, num in student:
    idx = num - 1
    if gender == 1:
        while idx < s_n:
            switch[idx] = 1 - switch[idx]
            idx += num
    else:
        switch[idx] = 1 - switch[idx]
        cnt = 1
        while True:
            if check(idx, cnt):
                if switch[idx - cnt] != switch[idx + cnt]:
                    break
            else:
                break
            cnt += 1
        for i in range(1, cnt):
            switch[idx + i] = 1 - switch[idx + i]
            switch[idx - i] = switch[idx + i]
for i in range(s_n):
    num = i + 1
    if num % 20:
        print(switch[i], end=' ')
    else:
        print(switch[i])
