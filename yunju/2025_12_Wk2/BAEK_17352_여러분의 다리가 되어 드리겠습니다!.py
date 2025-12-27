'''
N개의 섬
N-1개의 다리

1개 사라짐

어떤 두 섬 이으면 다시 모든 섬 왕복 가능할까?

떠오르는 생각
최소신장트리

'''

'''
이어진 것끼리 묶으면
두 묶음으로 나뉘어짐
각 묶음에서 하나씩 선택

!주의점!
작은 숫자를 부모로 잡았음
경우에 따라 부모의 최신화가 덜 되어있을 수 있음
>> 마지막에 find 다 돌려주어 해결
'''


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if px > py:
        parent[px] = py
    else:
        parent[py] = px
N = int(input())

parent = [0] + [i for i in range(1,N+1)]

for _ in range(N-2):
    a,b = map(int, input().split())
    union(a,b)

roots = set()
for i in range(1,N+1):
    roots.add(find(i))
print(*(roots))