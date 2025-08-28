N = int(input())
tree = {}

# 인자 입력 받기! 단어라서 편의를 위해 딕셔너리로 받음
for _ in range(N):
    p, left, right = input().split()
    tree[p] = [left, right]

# 전위순회 (루트가 1등)
def preorder(t):
    if t != '.':
        print(t, end='')
        preorder(tree[t][0])
        preorder(tree[t][1])

# 중위순회 (루트가 중간)
def inorder(t):
    if t != '.':
        inorder(tree[t][0])
        print(t, end='')
        inorder(tree[t][1])

# 후위순회 (루트가 마지막)
def postorder(t):
    if t != '.':
        postorder(tree[t][0])
        postorder(tree[t][1])
        print(t, end='')


# 출력하기
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()