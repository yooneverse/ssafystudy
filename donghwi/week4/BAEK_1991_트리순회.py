class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# 전위 순회(V L R)
def preorder(t):
    if t:
        print(t.value, end="")
        preorder(t.left)
        preorder(t.right)


# 중위 순회 (L V R)
def inorder(t):
    if t:
        inorder(t.left)
        print(t.value, end="")
        inorder(t.right)


# 후위 순회 (L R V)
def postorder(t):
    if t:
        postorder(t.left)
        postorder(t.right)
        print(t.value, end="")


N = int(input())
# 딕셔너리 생성
nodes = {}

for _ in range(N):
    P, child_l, child_r = input().split()

    # 노드를 생성한 적 없다면 생성
    if P not in nodes:
        nodes[P] = Node(P)  # {P: Node(P)}
    # 입력이 '.'가 아닌 경우
    if child_l != '.':
        nodes[child_l] = Node(child_l)  # {child_l: Node(child_l)}
        nodes[P].left = nodes[child_l]  # 왼쪽 연결
    if child_r != '.':
        nodes[child_r] = Node(child_r)  # {child_r: Node(child_r)}
        nodes[P].right = nodes[child_r]  # 오른쪽 연결

preorder(nodes['A'])
print()
inorder(nodes['A'])
print()
postorder(nodes['A'])