'''
두 샘플 무게 차이 잼

두 샘플의 무게 차이를 물어봄
지금까지 잰 결과 바탕으로 대답 가능하기도, 불가능하기도

어떤 두 샘플의 무게의 차이를 구할 수 있는지 없는지 알아내기
'''
'''
샘플 종류 2<= N <= 100000
상근이 일 수 1 <= M <= 100000

무게 쟀다면
! a b w : b 가 a보다 w 그램 무겁다 
w는 1000000 이하
'''
'''
여러 개가 이어져서 두 무게의 차이를 구해야 할 수도
>> 유니온 파인드
두 샘플 무게 차이 계산 가능 여부를 판단할 수 있음

루트노드를 찾는 parent 배열과
비교한 두 샘플 정보를 저장하는 배열?
그러면 너무 matrix의 사이즈가 커지는데 
총 무게 차를 연쇄적으로 계산하는 것도 웃기고
순서가 꼬일 수도. 안됨.
'''
'''
가중치 유니온 파인드

결국 최종적으로는 루트 노드
현재 노드와 루트노드간의 무게 차이 구할 수 있음


'''
import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x

    pre_parent = parent[x]
    parent[x] = find(parent[x])

    # 현재 노드부터 root까지 거리 갱신
    # 이전 부모까지 거리 + 부모~루트 거리
    dist[x] += dist[pre_parent]
    return parent[x]

def union(a,b,w):
    rootA = find(a)
    rootB = find(b)
    
    if rootA == rootB:
        return True
        
    if rank[rootA] > rank[rootB]:
        parent[rootB] = rootA
        dist[rootB] = dist[a] - dist[b] + w
        
    elif rank[rootA] < rank[rootB]:
        parent[rootA] = rootB
        dist[rootA] = dist[b] - dist[a] - w
        
    else:
        parent[rootB] = rootA
        rank[rootA] += 1
        dist[rootB] = dist[a] - dist[b] + w
        
    return False

    
while True:
    N,M = map(int, input().split())
    if N == M == 0:
        break
    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)
    dist = [0] * (N+1)
    # root와 본인의 무게 차이를 저장
    w_diff = [0] * (N+1)
    
    for _ in range(M):
        compare = list(input().split())
        if compare[0] == '!':
            a,b,c = map(int, compare[1:])
            union(a,b,c)

        else:
            a,b = map(int, compare[1:])
            if find(a) == find(b):
                print(dist[b] - dist[a])
            else:
                print("UNKNOWN")
            
            