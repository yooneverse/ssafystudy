# 1215. [S/W 문제해결 기본] 3일차 - 회문1
# import sys
# sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):
    length = int(input())       # 찾아야 하는 회문의 길이
    N = 8                       # 배열의 크기
    matrix = [list(input()) for _ in range(N)]
    # matrix를 전치행렬로 x-y 변환하여 찾기 쉽게 함
    matrix_trans = list(map(list, zip(*matrix)))
    cnt = 0                     # 찾은 회문의 개수

    for i in range(N):
        for j in range(N):
            # 탐색 범위가 N-1을 넘지 않도록
            if j + length <= N:
                # (i, j) 부터 x축 length 길이의 문장이 본인의 역과 같으면 회문으로 판단
                if matrix[i][j:j + length] == matrix[i][j:j + length][::-1]:
                    cnt += 1
                # (j, i) 부터 y축 length 길이의 문장이 본인의 역과 같으면 회문으로 판단
                if matrix_trans[i][j:j + length] == matrix_trans[i][j:j + length][::-1]:
                    cnt += 1

    print(f'#{tc} {cnt}')
