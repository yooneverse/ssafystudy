# BAEK 1991. 트리 순회
def preorder_traversal(t):  # 전위 순회
    if t:
        print(tree[t], end="")  # V
        # index()를 사용하는 이유:
        # c_l과 c_r에는 다음 노드의 정보가 들어있지만,
        # 다음 노드가 tree 의 몇 번째 원소인지 모른다.
        # 그래서 찾아주는 것이다.
        preorder_traversal(tree.index(c_l[t]))  # L
        preorder_traversal(tree.index(c_r[t]))  # R


def inorder_traversal(t):   # 중위 순회
    if t:
        inorder_traversal(tree.index(c_l[t]))   # L
        print(tree[t], end="")  # V
        inorder_traversal(tree.index(c_r[t]))   # R


def postorder_traversal(t): # 후위 순회
    if t:
        postorder_traversal(tree.index(c_l[t])) # L
        postorder_traversal(tree.index(c_r[t])) # R
        print(tree[t], end="")  # V

# 이진 트리의 노드의 개수 N
N = int(input())
# 노드 순서를 위한 부모 리스트
tree = [0] * (N + 1)
# 왼쪽/오른쪽 자식 리스트
c_l = [0] * (N + 1)
c_r = [0] * (N + 1)

# 입력값을 부모/자식 리스트에 나눠 담음
for i in range(1, N + 1):
    arr = list(map(str, input().split()))
    tree[i] = arr[0]
    if arr[1] != '.':
        c_l[i] = arr[1]
    if arr[2] != '.':
        c_r[i] = arr[2]

# 각각의 함수에서 문자열을 붙이는 방식으로(end="") 출력했으므로
# 함수 호출이 종료되면 줄바꿈을 위해 print() 사용
preorder_traversal(1)
print()
inorder_traversal(1)
print()
postorder_traversal(1)
