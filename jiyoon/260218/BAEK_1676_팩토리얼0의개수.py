import sys
input = sys.stdin.readline

n = int(input())

# N!에서 5의 개수만 세면 끝자리 0 개수와 같다
count = 0
div = 5

# 5, 25, 125 ... 로 나누며 5의 개수 누적
while div <= n:
    count += n // div
    div *= 5

print(count)
