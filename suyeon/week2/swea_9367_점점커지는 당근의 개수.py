import sys
sys.stdin = open('C:/Users/bsy40/OneDrive/Desktop/ssafystudy/suyeon/week2/IM/input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    carrots = list(map(int, input().split()))

    max_count = 0
    count = 1 # 구간의 최소 길이
    for i in range(n - 1): # 배열 범위 탈출 방지
        # 문제 잘 읽기: 연속적으로 커지기만 하면 됨, 순차적으로 1씩 커지는게 아니라
        if carrots[i] + 1 <= carrots[i + 1]: # 오른쪽과 비교하며 연속적인지 비교
            count += 1
        else: # 연속적이지 않을 때
            max_count = max(max_count, count)
            count = 1
    
    # 마지막 당근까지 확인 후 max 갱신이 안되므로 출력 시 한번 더 갱신
    print(f'#{test_case} {max(max_count, count)}')