import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
'''
문제
길이 N 수열
명령
1 i x : i번째 수(인덱스는 i-1)를 x 로 바꿈
2 l r : l번째 수부터 r번째 수 중 짝수 개수 출력
3 l r :    ''                 홀수 개수 출력
'''
'''
아이디어 
구간 내의 홀 수 또는 짝수의 개수 
>> 구간합 
>> 세그먼트 트리

홀수 개수에 대한 트리
짝수 개수에 대한 트리 
'''
'''
코드 줄이기

구간 내 홀수의 개수 = 구간 개 수의 개수 - 구간 내 짝수의 개수
'''

# 트리의 노드에 구간합을 저장
def init(node, left, right):
    if left == right:
        # oddtree[node] = odd[left]
        eventree[node] = even[left]
        return
    mid = (left+right) //2

    init(node*2, left, mid)
    init(node*2+1, mid+1, right)

    # oddtree[node] = oddtree[node*2]+oddtree[node*2+1]
    eventree[node] = eventree[node*2]+eventree[node*2+1]

# idx번째 숫자 변경
# 해당 수를 포함하는 구간합도 모두 업데이트
# 다만 홀수, 짝수의 개수이기 때문에 0과 1 -> XOR 사용
def update(node, start, end, idx):
    if idx < start or idx > end:
        return

    if start == end:
        # oddtree[node] ^= 1
        eventree[node] ^= 1
        return

    mid = (start+end) //2
    update(node*2, start, mid, idx)
    update(node*2+1, mid+1, end, idx)

    # oddtree[node] = oddtree[node*2]+oddtree[node*2+1]
    eventree[node] = eventree[node*2]+eventree[node*2+1]

# 구간 내 짝수의 개수
def evenquery(node, start, end, left, right):
    if right < start or left > end:
        return 0
    if left <= start and right >= end:
        return eventree[node]

    mid = (start+end) // 2

    leftSum = evenquery(node*2, start, mid, left, right)
    rightSum = evenquery(node*2+1, mid+1, end, left, right)

    return leftSum+rightSum

#
# def oddquery(node, start, end, left, right):
#     if right < start or left > end:
#         return 0
#     if start >= left and right >= end:
#         return oddtree[node]
#
#     mid = (start + end) // 2
#
#     leftSum = oddquery(node * 2, start, mid, left, right)
#     rightSum = oddquery(node * 2 + 1, mid + 1, end, left, right)
#
#     return leftSum + rightSum


N = int(input())
arr = list(map(int, input().split()))
# odd = [1 if x%2==1 else 0 for x in arr]
even = [1 if x%2==0 else 0 for x in arr]

# oddtree = [0 for _ in range(4*N)]
eventree = [0 for _ in range(4*N)]

init(1,0,N-1)

M = int(input())
for _ in range(M):
    p,q,r = map(int, input().split())
    if p == 1:
        if abs(arr[q-1]-r) % 2 != 0:
            update(1,0, N-1, q-1)
        arr[q-1] = r

    elif p == 2:
        ans = evenquery(1,0,N-1, q-1, r-1)
        print(ans)

    else:
        # ans = oddquery(1,0,N-1,q-1,r-1)
        ans = r-q+1 - evenquery(1,0,N-1,q-1,r-1)
        print(ans)


