T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    stones = list(map(int, input().split()))
 
    for i in range(m):
        start, change_num = map(int, input().split())
        color = stones[start - 1]
        for j in range(change_num):
            if start - 1 + j == n:
                break
            stones[start - 1 + j] = stones[start - 1]
    print(f'#{test_case}', *stones)