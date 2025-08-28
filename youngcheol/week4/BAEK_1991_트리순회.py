# 전위 순회(Root -> Left -> Right)

res = []


def preorder(i):
    if i == 0:
        return
    res.append(ch(i))
    preorder(left(i))
    preorder(right(i))


# 중위 순회(Left -> Root -> Right)
res1 =[]
def inorder(i):
    if i == 0:
        return

    inorder(left(i))
    res.append(ch(i))
    inorder(right(i))


# 후위 순회(Left -> Right -> Root)
res2 =[]
def postorder(i):
    if i == 0:
        return

    postorder(left(i))
    postorder(right(i))
    res.append(ch(i))


N = int(input())
ch = [0] * (N + 1)  # 노드번호 A부터 시작하기에 N+1
left = [0] * (N + 1)  # 왼쪽 자식 노드번호
right = [0] * (N + 1)  # 오른 쪽 자식 노드 번호

#여기서 영어를 어느 방식으로 바꿔서 넣어야할지 모르겠습니다.


root =

#전위 순회 결과 출력
preorder(root)
print(''.join(res))

#중위 순회 결과 
inorder(root)
print(''.join(res1))


#후위 순회 결과 
postorder(root)
print(''.join(res2))