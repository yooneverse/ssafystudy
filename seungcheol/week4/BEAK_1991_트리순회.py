import sys
sys.stdin = open("input.txt", "r")

# 전위 순회
def preorder(r):
    if r:
        print(lst[r][0], end="")
        root_l = dictionary[left[r]]
        preorder(root_l)
        root_r = dictionary[right[r]]
        preorder(root_r)

# 중위 순회
def inorder(r):
    if r:
        root_l = dictionary[left[r]]
        inorder(root_l)
        print(lst[r][0], end="")
        root_r = dictionary[right[r]]
        inorder(root_r)

# 후위 순회
def postorder(r):
    if r:
        root_l = dictionary[left[r]]
        postorder(root_l)
        root_r = dictionary[right[r]]
        postorder(root_r)
        print(lst[r][0], end="")

# 트리의 노드 개수 입력
N = int(input())

# 트리 정보를 받을 리스트
lst = [[0] for _ in range(N+1)]

# 노드의 부모 정보
parent = [0] * (N+1)

# 노드의 자식 정보
left = [0] * (N+1)
right = [0] * (N+1)

# 노드의 순서와 이름(영어)를 매칭할 딕셔너리
dictionary = {}

# 트리의 노드 정보를 입력받아 순서에 맞게 리스트와 딕셔너리에 저장
for i in range(1, N+1):
    lst[i] = list(input().split())
    dictionary[lst[i][0]] = i

# 이후 재귀함수에서 자식이 없는 경우 조회할 값 저장
dictionary[0] = 0

# 딕셔너리를 활용하여 부모 정보와 자식 정보 저장
for j in range(1, N+1):
    if lst[j][1] != ".":
        parent[dictionary[lst[j][1]]] = lst[j][0]
        left[dictionary[lst[j][0]]] = lst[j][1]
    if lst[j][2] != ".":
        parent[dictionary[lst[j][2]]] = lst[j][0]
        right[dictionary[lst[j][0]]] = lst[j][2]

# root 확인
for k in range(1, N+1):
    if parent[k] == 0:
        root = k
        break

preorder(root)
print()
inorder(root)
print()
postorder(root)
