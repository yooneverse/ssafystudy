T = int(input())

for tc in range(1, 1 + T):
    N = int(input())  # N개로 이루어진 수열
    arr = list(map(int, input().split()))

    # 2보다 크거나 같은 정수 하나 고르기
    # 첫번째 수를 N번째 수와 더하고 두번째 수를 N-1번째 수와 더하는 형식
    # 새로운 수열 생성
    # N이 홀수인 경우 가운데 수를 자기 자신과 더한다.
    # 수열이 두개가 포함되어 있으면 첫번째 수가 두번째 수보다 큰 경우 상근이 승
    # 나머지 경우 창영이 승

    while len(arr) > 2:  #arr의 길이가 2보다 클때 동안 반복
        n = len(arr)
        nxt = [arr[i] + arr[n - 1 - i] for i in range(n // 2)]
        if n % 2 == 1:  # 만약 2로 나눴을때 1이 남으면
            nxt.append(arr[n // 2] * 2)  # 중간값은 2번더해줘서 넣어준다.
        arr = nxt

    if arr[0] > arr[1]:
        winner = "Alice"
    else:
        winner = "Bob"
    print(f"Case #{tc}: {winner}")