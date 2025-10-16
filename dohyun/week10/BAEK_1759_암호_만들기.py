# BAEK 1759. 암호 만들기
L, C = map(int, input().split())
alphabet = list(map(str, input().split()))
# 알파벳이 암호에서 증가하는 순서
# 오름차순 정렬
alphabet.sort()

# 모음 리스트
vowel = ['a', 'e', 'i', 'o', 'u']


# 최소 한 개의 모음, 최소 두 개의 자음 판별 함수
def is_valid(arr):
    cnt = 0     # 모음 개수
    for a in arr:
        if a in vowel:
            cnt += 1
    # 모음이 한 개 이상이고, L-2개 이하여야 한다
    if 1 <= cnt <= L - 2:
        return True
    return False


def find_password(cnt, arr, start):
    # L개의 알파벳이 모이면 비밀번호 판별
    if cnt == L:
        if is_valid(arr):
            for a in arr:
                print(a, end='')
            print(end='\n')
        return

    # 순열 재귀
    for i in range(start, C):
        arr.append(alphabet[i])
        find_password(cnt + 1, arr, i + 1)
        arr.pop()


find_password(0, [], 0)