T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    while len(arr) > 2:
        new_arr = []
        # 앞뒤 더하기
        for i in range(len(arr)//2):
            new_arr.append(arr[i] + arr[-1-i])
        # 홀수 처리 (가운데 원소는 자기 자신 2배)
        if len(arr) % 2 == 1:
            mid = len(arr)//2
            new_arr.append(arr[mid] * 2)
        arr = new_arr

    # 최종 승자 판별
    if arr[0] > arr[1]:
        print(f"Case #{tc}: Alice")
    else:
        print(f"Case #{tc}: Bob")