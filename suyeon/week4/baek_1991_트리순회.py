PARENT = {}
LEFT_CHILD = {}
RIGHT_CHILD = {}


def find_root(node):
    while PARENT.get(node):  # node(child)와 연결된 부모가 있나 -> 없으면 멈춤
        node = PARENT[node]  # 있으면 부모로 올라가기
    return node


def preorder(root):
    if root is not None:
        print(root, end='')
        # 딕셔너리에 없는 키를 호출할 경우 keyerror
        # keyerror 대신 None을 반환하기 위해 .get() 사용
        preorder(LEFT_CHILD.get(root))
        preorder(RIGHT_CHILD.get(root))


def inorder(root):
    if root is not None:
        inorder(LEFT_CHILD.get(root))
        print(root, end='')
        inorder(RIGHT_CHILD.get(root))


def postorder(root):
    if root is not None:
        postorder(LEFT_CHILD.get(root))
        postorder(RIGHT_CHILD.get(root))
        print(root, end='')


n = int(input())

# 노드 연결 상태 기입
for _ in range(n):
    parent, left, right = input().split()
    if left != '.':
        PARENT[left] = parent
        LEFT_CHILD[parent] = left

    if right != '.':
        PARENT[right] = parent
        RIGHT_CHILD[parent] = right

# 루트 찾기
root_node = find_root('A')  # 아무거나 넣음

# 찾은 루트부터 순회하기
preorder(root_node)
print()
inorder(root_node)
print()
postorder(root_node)
