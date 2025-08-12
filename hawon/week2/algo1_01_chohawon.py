# N x N 공간에 M x M 영역을 탐색
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # 원하는 좌표
    star = []
    for r in range(N-M+1):
        for c in range(N-M+1):
            now = []
            count = 0
            for i in range(M):
                for j in range(M):
                    if arr[r+i][c+j] == '*':
                        count += 1
                        now.append([r+i, c+j])
        if count == K:
            star = now[0]
            print(f'#{tc} {star}')
        else:
            print(-1, -1)


        # 이제 별이 원하는 값일 때의 좌표를 출력해야 함