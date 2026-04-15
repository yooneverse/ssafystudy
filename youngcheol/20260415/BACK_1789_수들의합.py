s = int(input())

total = 0
cnt=0

# 1부터 차근차근 더해보자
for i in range(1, s + 1):
    total += i
    cnt += 1
    
    # 더한 값이 S보다 커지면 끝
    if total > s:
        cnt -= 1
        break

print(cnt)