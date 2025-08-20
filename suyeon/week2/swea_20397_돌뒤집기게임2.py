def flip_stone(reverse_num):
    global n, stones
    for _ in range(reverse_num):
        i, j = map(int, input().split()) # i - 1이 문제에서 원하는 인덱스 위치
        for distance in range(1, j + 1):
            left = i - 1 - distance
            right = i - 1 + distance
            if left < 0 or right >= n:
                break
            else:
                if stones[left] == stones[right]:
                    # ^= : 비트 단위 XOR 연산자
                    # 비트가 서로 다른 경우에만 1, 같으면 0
                    # 만약 stones[left] = 1이면
                    #   000001 (= stones[left])
                    # ^ 000001
                    # = 000000 = 0 이되어서 즉 우리가 원하는 1 -> 0으로 바꿀 수 있는 것
                    # 만약 stones[left] = 0이면
                    #   000000 (= stones[left])
                    # ^ 000001
                    # = 000001 = 1 이되어서 즉 우리가 원하는 0 -> 1로 바꿀 수 있는 것
                    stones[left] ^= 1
                    stones[right] ^= 1
                    
T = int(input())
for test_case in range(1, 1+T):
    n, m = map(int, input().split()) # n = 돌의 수, m = 뒤집기 수
    stones = list(map(int, input().split()))

    flip_stone(m)

    print(f'#{test_case}', *stones)

