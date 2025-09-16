T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    while len(arr) > 2:
        new_arr = []

        # 양끝끼리 더하기
        for i in range(len(arr) // 2):
            new_arr.append(arr[i] + arr[-1 - i])

        # 홀수라면 가운데 자기 자신 더하기
        if len(arr) % 2 == 1:
            mid = arr[len(arr) // 2]
            new_arr.append(mid + mid)

        arr = new_arr

    # 마지막 두 수 비교
    if arr[0] > arr[1]:
        winner = "Alice"
    else:
        winner = "Bob"

    # 출력 형식 수정
    print(f"Case #{tc}: {winner}")
