import sys
sys.stdin = open("sample_in.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 지도의 크기 입력
    N = int(input())

    # 지도의 높이 정보
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 최대 길이
    max_distance = 0

    # delta
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]





    for i in range(N):
        for j in range(N):
            # while 문 안에서 시작위치, 다음 이동 위치
            si = ei = i
            sj = ej = j
            # while 종료 조건, while 전 True로 초기화
            flag = True
            # 이동 거리
            cnt = 1
            while flag:
                # 가장 낮은 위치 시작위치로 초기화
                lower = matrix[si][sj]
                for d in range(4):
                    ni = si + di[d]
                    nj = sj + dj[d]
                    # 이동 위치가 인덱스 범위 안이면서 lower보다 낮으면
                    if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] < lower:
                        # lower 갱신, 다음 위치 변경
                        lower = matrix[ni][nj]
                        ei, ej = ni, nj
                # 4방향 확인 후 다음 위치가 시작 위치와 동일하면 이동이 불가능한 것이므로 반복 종료
                if si == ei and sj == ej:
                    flag = False
                # 반복 가능하면 시작 위치 변경 및 이동거리 1 증가
                else:
                    si, sj = ei, ej
                    cnt += 1
            # while이 끝나면 최대 이동거리와 비교
            if max_distance < cnt:
                max_distance = cnt

    print(f"#{test_case} {max_distance}")