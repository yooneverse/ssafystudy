import sys
sys.stdin = open('C:/Users/bsy40/OneDrive/Desktop/ssafystudy/suyeon/week2/IM/input.txt', 'r')

def sum_of_row(arr):
    sums = []
    for row in arr:
        sums.append(sum(row))
    return sums

def sum_of_col(arr):
    # zip: iterabel 변수들을 같은 인덱스끼리 튜플로 묶은 이터레이터 반환
    # 예) stage = [[1,2,3], [4,5,6]]
    # *stage(언패킹) = [1,2,3], [4,5,6]
    # zip(*stage) = zip([1,2,3], [4,5,6]) 이게 곧 (1,4),(2,5),(3,6)
    # list(zip(*stage)) = [(1,4),(2,5),(3,6)]
    trans_stage = list(zip(*arr))
    sums = []
    for col in trans_stage:
        sums.append(sum(col))
    return sums


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    stage = [list(map(int, input().split())) for _ in range(n)]

    # 결국 행의 합과 열의 합을 비교하는 것이므로
    # 동일한 행에 있거나 동일한 열에 있으면 위치가 어디든 합이 같을 것
    row_sums = sum_of_row(stage)
    col_sums = sum_of_col(stage)

    max_pang = 0
    # 문제에서 주어진 입력 사항에서 aij의 최대값 = 9
    # aij의 최대값이 9 일 때 얻을 수 있는 최대 점수 = 한 행과 한 열에 9가 n개씩 있을 때
    # 9(최대값) * n(개) * 2(행, 열)
    min_pang = 9 * n * 2
    for i in range(n):
        for j in range(n):
            pang = row_sums[i] + col_sums[j] - stage[i][j] # 기준 위치 값이 두번 포함되므로 한번 빼줌
            if max_pang < pang:
                max_pang = pang
            
            if min_pang > pang:
                min_pang = pang

    # 스테이지의 점수는 두 점수 간의 차이이므로 차이가 클수록 점수가 높음
    print(f'#{test_case} {max_pang - min_pang}')