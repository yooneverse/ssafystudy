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

멀티탭이 꽉 찬 상태에서 무엇을 뽑을 것인가.
현 시점 기준 재사용 시기가 가장 늦는 것(없는 것)

재사용 시점을 어떻게 알아낼 것인가?
1. 남은 제품들 순회하며 제품별 idx를 비교하여 가장 나중에 등장하는 것을 선택
2. 미리 제품별 idx를 기록 (딕셔너리)
'''
'''
결과
메모리: 34968 KB
시간: 60 ms

시간이 전부 순회했던 풀이보다 더 걸림
K가 더 커지면 의미 있을 듯
'''
from collections import defaultdict

N, K = map(int, input().split())

# 멀티탭에 꽂힌 전기 용품 관리
multi = []

# 전기 용품 사용 순서
order = list(map(int, input().split()))

# 제품별 등장 순서 기록
use_idx = defaultdict(list)

# 제품 번호 별로 등장 idx를 순서대로 기록
for i in range(K):
    product = order[i]
    use_idx[product].append(i)

# 뽑는 총 횟수
ans = 0

# K번의 순서 따라가며 시행
for i in range(K):
    # i번째 제품
    product = order[i]

    # i번째 제품의 등장 idx를 빼냄 (현재 기준 남은 일정만 남김)
    # [1번,3번,5번] 꽂아야 했다면 1번 꽂고 [3번,5번]만 남도록
    use_idx[product].pop(0)
    
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

    # 현재 멀티탭에 꽂혀 있는 것들 하나씩 확인
    for plug in multi:
        # 앞으로 쓸 예정이 없는 코드는 바로 뽑고 넘어감
        if not use_idx[plug]:
            out_product = plug
            break
        
        # 꽂힌 제품별 순서 비교
        # 가장 나중에 쓰이는 제품을 뽑음 
        idx = use_idx[plug][0]
        if out_idx < idx:
            out_idx = idx
            out_product = plug
    # 뽑고
    multi.remove(out_product)
    # 꽂고
    multi.append(product)
    # 횟수 추가
    ans += 1
print(ans)