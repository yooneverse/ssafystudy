N = int(input())

total = -1  # 못 만들 경우를 대비해 -1로 초기화

five_cnt = N // 5  # 5kg 봉지 최대 개수

while five_cnt >= 0:
    left = N - (five_cnt * 5)  # 남은 무게
    if left % 3 == 0:  # 3으로 나누어떨어지는지 확인
        total = five_cnt + (left // 3)
        break
    five_cnt -= 1

print(total)
