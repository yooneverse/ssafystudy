# 전위순회
def preorder(v):
    if v != 0:                     # 0이면 자식 없음
        print(value[v], end="")
        preorder(left[v])
        preorder(right[v])

# 중위순회
def inorder(v):
    if v != 0:
        inorder(left[v])
        print(value[v], end="")
        inorder(right[v])

# 후위순회
def postorder(v):
    if v != 0:
        postorder(left[v])
        postorder(right[v])
        print(value[v], end="")

N = int(input())  # 노드 개수

value = [""] * (N + 1)
left = [0] * (N + 1)
right = [0] * (N + 1)
nodes = {}      # 문자 → 인덱스
idx = 1         # 1부터 시작 (0은 없음 표시)

for _ in range(N):
    p, l, r = input().split()

    # 부모 등록
    if p not in nodes:                  # 만약 부모 문자가 아직 번호가 없으면
        nodes[p] = idx                  # 새 번호(idx)를 배정 (A=1, B=2 … 순서대로)
        value[idx] = p                  # value[idx]에 문자 저장 → 번호→문자 매핑
        idx += 1                        # 다음 새 노드는 다음 번호로
    pi = nodes[p]                       # 부모 문자의 인덱스 번호를 pi에 저장

    # 왼쪽 자식 등록
    if l != '.':                        # 왼쪽 자식이 '.'이 아니면 (자식 있음)
        if l not in nodes:              # 자식 문자가 아직 등록되지 않았다면
            nodes[l] = idx              # 새 번호 배정
            value[idx] = l              # 해당 번호 위치에 문자 저장
            idx += 1                    # 다음 번호 준비
        left[pi] = nodes[l]             # 부모 인덱스 pi의 왼쪽 자식에 등록된 번호 연결

    # 오른쪽 자식 등록
    if r != '.':                        # 오른쪽 자식이 '.'이 아니면 (자식 있음)
        if r not in nodes:              # 자식 문자가 아직 등록되지 않았다면
            nodes[r] = idx              # 새 번호 배정
            value[idx] = r              # 해당 번호 위치에 문자 저장
            idx += 1                    # 다음 번호 준비
        right[pi] = nodes[r]            # 부모 인덱스 pi의 오른쪽 자식에 등록된 번호 연결

# 루트는 항상 'A'
root = nodes['A']
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()

# 모범답안으로 추정되는 딕셔너리 방법

def preorder(v):
    if v != '.':
        print(v, end="")
        preorder(tree[v][0])
        preorder(tree[v][1])

def inorder(v):
    if v != '.':
        inorder(tree[v][0])
        print(v, end="")
        inorder(tree[v][1])

def postorder(v):
    if v != '.':
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end="")

N = int(input())
tree = {}

for _ in range(N):
    p, l, r = input().split() #v로 안 보고 부모라는 뜻의 p로 할당
    tree[p] = (l, r)

# 항상 'A'부터 시작
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
