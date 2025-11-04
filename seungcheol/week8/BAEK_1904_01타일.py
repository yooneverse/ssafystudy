N = int(input())

if N < 3:
    print(N)
else:
    prev1 = 1
    prev2 = 2

    for i in range(N - 2):
        # 수가 크면 +연산 느려져서 시간초과가 생기므로
        # %연산을 통해 자릿수 줄이기
        prev1, prev2 = prev2, (prev2 + prev1) % 15746

    print(prev2)