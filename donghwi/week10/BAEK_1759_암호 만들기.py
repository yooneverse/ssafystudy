# 조건 1. 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
# 조건 2. 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열 예) abc 가능, bac 불가능

# 조건 1 판별 함수
def check(word):
    c_cnt = 0
    v_cnt = 0
    for s in word:
        # 자음 이면
        if s in consonant:
            c_cnt += 1
        # 모음 이면
        else:
            v_cnt += 1
    # 조건 1이 만족 하면 True, 아니면 False
    if c_cnt >= 2 and v_cnt >= 1:
        return True
    else:
        return False


def search(idx, password):
    if idx == L:
        if check(password):
            print(password)
        return

    for i in range(C):

        if password:
            if ord(password[-1]) >= ord(lst[i]):
                continue

        if visited[i]:
            continue

        visited[i] = 1
        search(idx + 1, password + lst[i])
        visited[i] = 0


L, C = map(int, input().split())
consonant = "bcdfghjklmnpqrstvwxyz"
vowel = "aeiou"
lst = list(input().split())
visited = [0] * C
lst.sort()
search(0, '')
