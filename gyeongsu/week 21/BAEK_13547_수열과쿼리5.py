import math

# 제곱근 분할
# 오프라인 쿼리
# mo's 알고리즘



# 1. 제곱근 분할
# 10만까지의 범위를 sqrt(10)만의 블럭을 생성하여 각 블럭에 저장

# 2. 오프라인 쿼리
# 뒤죽박죽인 쿼리를 계산하기 유리하게 정렬하여 답을 도출

# 3. 모스 알고리즘
# 2번에서 언급한 계산하기 유리하게 정렬하는 아이디어
# 왼쪽 블럭이 홀수 일때는 오름차순 짝수일 때는 내림차순으로 정렬하여 지그재그로 쿼리에 대한 답을 도출


# 입력 최적화
import sys
input = sys.stdin.readline 


# 수열의 길이와 수열 입력
N = int(input())
arr = list(map(int, input().split()))
sqrtN = int(math.sqrt(N)) # 크기 N의 제곱근 <- 분할의 기준 0~(sqrtN-1) 까지  0번 블럭



# 쿼리 갯수 입력
Q = int(input())

# 쿼리 입력
Querys = [None] * Q # 쿼리 모음 객체 초기화
for i in range(Q):
    # 각 쿼리는 [시작 인덱스, 종료 인덱스, 질문의 순서, 블럭]
    s, e = map(int, input().split())
    block = s // sqrtN
    Querys[i] = [s-1, e-1, i, block]
    
# 쿼리를 모스 알고리즘에 맞게 정렬
Querys.sort(key = lambda x: (x[3], -x[1] if x[3] % 2 == 0 else x[1]))


# 정답 도출에 필요한 배열 초기화
# 정답 배열 초기화
ans = [-1] * Q
cAns = 0 # 서로 다른 수
freq = [0] * (1_000_005) # 각 인덱스 값의 빈도 수

# 포인터 탐색으로 갯수 세기

# 포인터 탐색 함수 정의


def add(val) -> None:
    """
    더하기 함수
    val : 추가 되는 값
    조건) 추가 되는 값이 0 이었다면 서로 다른수 ++ 됨.
    
    """
    global cAns
    if freq[val] == 0:
        cAns += 1
    freq[val] += 1

    
def remove(val) -> None:
    """
    빼기 함수
    val : 삭제 되는 값
    조건) 삭제 되는 값이 0으로 간다면 서로 다른수 -- 됨.
    """
    global cAns
    freq[val] -= 1
    if freq[val] == 0:
        cAns -= 1


cLeft, cRight = 1, 0

for i in range(Q):
    q = Querys[i]
    idx = q[2]
    left, right = q[0], q[1]
    # 왼쪽 기준 탐색 하고 있는 범위가 탐색 해야할 범위 보다 더 좁은 경우 확장해야함.
    while(cLeft > left):
        cLeft -= 1
        add(arr[cLeft])
    # 우측 기준 탐색 하고 있는 범위가 탐색 해야할 범위 보다 더 넓은 경우.
    while(cRight < right):
        cRight += 1
        add(arr[cRight])
    # 좌측 기준 탐색 하고 있는 범위가 탐색 해야할 범위보다 넓은 경우 -> 축소 해야함.
    while(cLeft < left):
        remove(arr[cLeft])
        cLeft += 1
    while(cRight > right):
        remove(arr[cRight])
        cRight -= 1
    
    ans[idx] = cAns
    

for i in range(Q):
    print(ans[i])
    
        