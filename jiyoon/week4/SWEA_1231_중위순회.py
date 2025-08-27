# 틀린 코드입니다. 비교를 위해 전부 첨부해둡니다.

T = int(input())  # 테스트 케이스 수

# 완전 이진 트리에 집중했을 때

# 중위순회하며 트리에 값 채우기
def in_order(n):
    global value
    if n <= N:
        in_order(n * 2)  # 왼쪽 자식
        tree[n] = value  # 현재 노드에 값 기록
        value += 1
        in_order(n * 2 + 1)  # 오른쪽 자식


# 중위순회하며 출력 문자열 만들기
def show(n):
    global ans
    if n <= N:
        show(n * 2)  # 왼쪽 자식
        ans.append(str(tree[n]))  # 현재 노드 값 추가
        show(n * 2 + 1)  # 오른쪽 자식


for tc in range(1, T + 1):
    N = int(input())  # 노드 개수

    # 근데 정점 정보가 V, L, R 순으로 들어옴
    # 이것을 어떻게 헤쳐나가는가!
    tree = [0] * (N + 1)  # 트리 노드 값 저장용 배열
    value = 1  # 채워 넣을 시작 값

    in_order(1)  # 루트(1)부터 중위순회하며 값 채우기

    ans = []  # 출력 문자열 저장용 리스트
    show(1)  # 루트부터 중위순회하며 값 수집

    # 리스트 -> 문자열 (for문 방식)
    word = ""
    for x in ans:
        word += x

    print(f"#{tc}", word)

# 정답 코드
# 완전 이진 트리에 매몰되지 말고, input이 어떻게 주어지는지 보고 풀기

T = 10  # 테스트 케이스 수 고정, 입력이 아니라 그냥 주어짐


# 중위순회 함수 (L -> V -> R)
def inorder(v):
    if v:                     # v가 0이면 자식이 없다는 뜻이므로 종료
        inorder(left[v])      # 왼쪽 자식 방문
        print(value[v], end="")   # 현재 노드 출력
        inorder(right[v])     # 오른쪽 자식 방문

for tc in range(1, T+1):
    N = int(input())  # 각 케이스의 N으로 노드 개수 주어짐

    # 배열 초기화
    value = [""] * (N + 1)   # 노드 번호별 문자 저장
    left = [0] * (N + 1)     # 왼쪽 자식 저장
    right = [0] * (N + 1)    # 오른쪽 자식 저장

    # 여기서 정점 정보가 들어오는 형식에 집중해야 함
    # 정점 정보는 노드 번호(V), 문자, L, R 순으로 들어옴
    for _ in range(N):
        nodes = input().split()
        # # 입력 줄의 첫 번째 값은 노드 번호
        # 여기서 다른 값을 가져와버리면 배열에 값을 넣을 기준이 뒤죽박죽이라서 순회가 꼬임
        v = int(nodes[0])           # 이 번호를 기준으로 value, left, right 배열에 값 저장
        value[v] = nodes[1]         # 두 번째 값은 노드에 저장된 문자
        # nodes를 경우에 따라 분배
        # len(nodes)가 2인 경우는 자식 없음, left[v], right[v]는 기본값 0 유지
        # 시험에서는 경우를 적고, pass 하는 것이 맞을듯
        if len(nodes) == 3:
            left[v] = int(nodes[2])
        elif len(nodes) == 4:
            left[v] = int(nodes[2])
            right[v] = int(nodes[3])

    # 중위순회 실행
    print(f"#{tc}", end=" ")
    inorder(1)  # 루트(1)부터 중위순회 시작
    print()
