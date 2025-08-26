n = int(input())

# 5kg 봉지를 제일 많이 들고 갈 것
# 5kg 봉지를 최대로 들었을 때 무게를 못 맞추면
# 하나씩 줄이면서 나머지를 3kg로 다 들 수 있는지 확인하면 됨
count = n // 5
for i in range(count, -1, -1):
    rest = n - (i * 5)
    if rest % 3 == 0:
        bongdary = i + (rest // 3)
        print(bongdary)
        break
# 5kg 없이 3kg로만 들고가는 것도 해봤는데
# 들고 갈 수 없더라
else:
    print(-1)