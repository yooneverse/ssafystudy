# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
# https://swexpertacademy.com/main/talk/solvingClub/problemPassedUser.do?contestProbId=AV14ABYKADACFAYh&solveclubId=AZhdubEaIe3HBIT9&problemBoxTitle=0807_List2&problemBoxCnt=6&probBoxId=AZiB15-a_6bHBIT9

# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):     # 10개의 케이
    T = int(input())
    # 100 x 100 배열 생성
    ladder = [list(map(int, input().split())) for _ in range(100)]

    result = 0      # 결과값
    for j in range(100):        # 가로열로 진행하며 반복
        if ladder[0][j] == 1:   # 사다리의 첫 번째 줄에서 시작점 찾기
            x, y = j, 0         # 가로 세로 변수 할당
            while y < 99:       # 높이가 99 미만일 때
                # 배열의 범위인 100을 넘지 않으면서 오른쪽으로 갈 수 있으면
                if x+1 < 100 and ladder[y][x+1] == 1:
                    # 갈 수 있는 만큼 오른쪽으로 이동
                    while x+1 < 100 and ladder[y][x+1] == 1:
                        x += 1
                # 배열의 범위인 0을 넘지 않으면서 왼쪽으로 갈 수 있으면
                elif x-1 >= 0 and ladder[y][x-1] == 1:
                    # 갈 수 있는 만큼 왼쪽으로 이
                    while x-1 >= 0 and ladder[y][x-1] == 1:
                        x -= 1
                # 그 외에는 아래로 이동
                y += 1
            # 사다리의 목적지에 도달하면 가로 좌표를 결과값에 할당
            if ladder[y][x] == 2:
                result = j

    print(f'#{tc} {result}')
