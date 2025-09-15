T = int(input())

for tc in range(1, 1 + T):
    N = int(input())

    lst = list(map(int, input().split()))

    # 순열을 접어서 2개가 남으면 종료
    while len(lst) > 2:
        length = len(lst)
        # 접은 순열을 담을 임시 리스트
        # // 연산은 소숫점에서 버려지므로 홀수의 경우 가운데부분이 버려짐
        # +1을 통해 가운데 부분 살림
        tmp = [0] * (length // 2 + 1)

        for i in range(length // 2 + 1):
            tmp[i] = lst[i] + lst[length - 1 - i]

        lst = tmp

    if lst[0] > lst[1]:
        print(f"Case #{tc}: Alice")
    else:
        print(f"Case #{tc}: Bob")