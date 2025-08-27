import sys
sys.stdin = open('C:/Users/bsy40/OneDrive/Desktop/ssafystudy/suyeon/input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    img = [list(map(int, input().split())) for _ in range(n)]
    trans_img = list(zip(*img))

    len = 0
    max_len = 0
    for i in range(n):
        len = 0
        for j in range(m - 1):
            if img[i][j]:
                len += 1
                if not img[i][j + 1]:
                    max_len = max(max_len, len)
                    len = 0

        if img[i][-1]:
            len += 1
            max_len = max(max_len, len)

    
    for i in range(m):
        len = 0
        for j in range(n - 1):
            if trans_img[i][j]:
                len += 1
                if not trans_img[i][j + 1]:
                    max_len = max(max_len, len)
                    len = 0
        
        if trans_img[i][-1]:
            len += 1
            max_len = max(max_len, len)
    
    if max_len < 2:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} {max_len}')