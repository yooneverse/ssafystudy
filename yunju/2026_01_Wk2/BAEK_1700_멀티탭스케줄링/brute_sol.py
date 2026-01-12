'''
한 개의 멀티탭
플러그 빼는 횟수 최소화
고정된 제품 사용 순서

동일 제품을 나중에 다시 사용해야 하는 경우 코드를 빼지 않아도 됨

멀티탭 구멍 수 1 <= N <= 100
전기용품 사용 횟수 1 <= K <= 100
'''
'''
아이디어
플러그를 최대한 안 빼야 한다

플러그는 언제 빼야 하는가?
꽉 찬 상태에서 다음 것을 꽂아야 할 때

어떤 것을 뽑는 것이 최선인가?
현시점 기준 추후 사용 횟수가 최소인 것?

!! 재사용 시기가 중요.
한참 뒤에 많이 사용하게 된다면 
아무리 많이 사용되더라도 뽑는 게 유리
'''
'''
결과
메모리: 32544 KB
시간: 32 ms
'''

N, K = map(int, input().split())

# 멀티탭에 꽂힌 전기 용품 관리
multi = []

# 전기 용품 사용 순서
order = list(map(int, input().split()))

# 뽑는 총 횟수
ans = 0

# K번의 순서 따라가며 시행
for i in range(K):
    product = order[i]

    # 이미 멀티탭에 있다면 다음으로
    if product in multi:
        continue

    # 멀티탭에 빈 칸이 있다면 꽂기
    if len(multi) < N:
        multi.append(product)
        continue

    # 멀티탭이 가득 차 있다면?
    # 누구를 뺄 것인가
    # 현 시점 기준 가장 나중에 쓰일 녀석
    out_product = -1
    out_idx = -1

    # 현 시점 기준 남은 것들
    remain = order[i+1:]

    # 뽑을 제품 정해졌는지 여부
    # 남은 일정 중에 없다면 나머지 제품 다 확인하지 않고 바로 뽑기 위해
    find = False

    # 현재 멀티탭에 꽂혀 있는 것들 하나씩 확인
    for plug in multi:
        # 경우 1
        # 남은 일정 중에 없다면 바로 뽑기
        if plug not in remain:
            multi.remove(plug)
            multi.append(product)
            ans += 1
            find = True
            break

        # 경우 2
        # 가장 나중에 사용될 제품을 뽑음
        # index 메서드
        # 리스트나 문자열에서 특정 값이 '처음' 나타나는 인덱스를 반환
        idx = remain.index(plug)
        if idx > out_idx:
            out_idx = idx
            out_product = plug

    # 경우 1에서 이미 처리가 끝난 경우
    if find:
        continue

    # 뺄 거 빼고
    multi.remove(out_product)
    # 새로 꽂고
    multi.append(product)
    # 횟수 추가
    ans += 1

print(ans)