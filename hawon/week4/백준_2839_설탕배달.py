N = int(input())
a, b = 3, 5

cnt = 0


# N이 0이 될때까지
while N >= 0:
    # 만약 n이 5의 배수이면
    if N % b == 0:
        # N을 5로 나눈 값을 cnt에 입력하고 바로 cnt 출력한다
        cnt += N // b
        print(cnt)
        break
    # 아니면 3을 빼주고 다시 반복.
    N -= a
    cnt += 1
# 다 했는데 둘 다 아니면 -1 출력하기
else:
    print(-1)