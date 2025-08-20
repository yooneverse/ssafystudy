T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())  # 회문의 길이
    plate = [input() for _ in range(8)]
 
    # 행 순회
    row_pal = 0
    for i in range(8):
        for j in range(8 - n + 1):
            for k in range(n // 2):  # 글자수 길이의 절반만큼 반복
                if plate[i][j + k] != plate[i][(j + n) - 1 - k]:
                    break
            else:
                row_pal += 1
 
    # 열 순회
    col_pal = 0
    for j in range(8):
        for i in range(8 - n + 1):
            for k in range(n // 2):
                if plate[i + k][j] != plate[(i + n) - 1 - k][j]:
                    break
            else:
                col_pal += 1
    print(f'#{test_case} {row_pal + col_pal}')