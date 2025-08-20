# 16585. 5일차 - 토너먼트 카드게임
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    # 가위/바위/보 판별 dict
    rcp = {1: '가위', 2: '바위', 3: '보'}
    # 토너먼트 대진 나누는 분할정복 함수
    def tournament(i, j):
        # 더 이상 나눌 수 없으면 값 반환(재귀 중단)
        if i == j:
            return i
        else:
            # mid = (i + j) // 2
            # 연속 구간을 정확하고 균형 있게 둘로 나누는 가장 단순한 기준
            # 왼쪽: [i, mid]/ 오른쪽: [mid + 1, j]
            # 정확히 1명까지 줄어드는 재귀가 보장됨
            left = tournament(i, (i + j) // 2)
            right = tournament((i + j) // 2 + 1, j)
            # left, right 값이 모두 나왔으니 battle 함수 실행
            return battle(left, right)
    # 대진에 따라 가위바위보하는 함수
    def battle(l, r):
        # 가위/바위/보 판별 dict 사용하기 위한 변수 할당
        l_num = cards[l]
        r_num = cards[r]
        # 가위 <- 바위 <- 보 <- 가위 순으로 설정
        # 만약 비길 시, 작은 쪽(left)이 승리
        if rcp[l_num] == '가위':
            if rcp[r_num] == '바위':
                return r
            else:
                return l

        elif rcp[l_num] == '바위':
            if rcp[r_num] == '보':
                return r
            else:
                return l

        elif rcp[l_num] == '보':
            if rcp[r_num] == '가위':
                return r
            else:
                return l
    # cards 리스트 인덱스 범위만큼 함수 인자로 할당
    winner = tournament(0, N - 1)
    # 1등의 번호는 인덱스 값 + 1
    print(f'#{tc} {winner + 1}')
