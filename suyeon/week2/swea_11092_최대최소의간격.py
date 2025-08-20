MAX_Ai = 10
MIN_Ai = 1

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    # arr[0]으로 초기화 하면, arr[0]이 최소값일 때 min_idx값 갱신 불가(지금 코드 기준)
    max_num = MIN_Ai
    min_num = MAX_Ai
    for i in range(n):
        if max_num <= arr[i]:
            max_num = arr[i]
            max_idx = i + 1 # 문제에서 인덱스 1부터 셈

        if min_num > arr[i]:
            min_num = arr[i]
            min_idx = i + 1
    
    print(f'#{test_case} {max(max_idx, min_idx) - min(max_idx, min_idx)}')