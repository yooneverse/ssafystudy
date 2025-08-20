# 1057. 토너먼트
N, M, K = map(int, input().split())
# N명의 참가자 배열 생성
row = list(range(N))
cnt = 0     # 라운드 수
# 지민이와 한수의 라운드를 기록하는 함수
def tournament(i, j):
    global cnt  # 전역 변수 생성
    # 지민이와 한수가 만나면 재귀 중단
    if i == j:
        return
    # 서로 만나는 지점을 확인하기 위한 계산
    # ex) 1, 2번 대결 -> 1번으로 통일됨 / 7, 8번 대결 -> 4번으로 통일됨
    # 그렇게 16강 -> 8강 -> 4강 -> ... 점점 줄어들며 같은 수가 되면 대결 성사
    else:
        i, j = (i + 1) // 2, (j + 1) // 2
        # 라운드 수를 증가시키고 재귀 호출
        cnt += 1
        tournament(i, j)
# 지민이와 한수의 번호로 함수 호출
tournament(M, K)
print(cnt)