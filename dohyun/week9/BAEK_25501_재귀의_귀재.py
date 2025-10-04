# BAEK 25501. 재귀의 귀재
T = int(input())


# 재귀 함수 정의
# 인자로 문자열, 왼쪽 좌표, 오른쪽 좌표, 재귀 횟수 받음
def recursion(char, l, r, cnt):
    # 좌표가 교차하거나 같아지면 1과 재귀 횟수 반환
    if l >= r:
        return 1, cnt
    # 양쪽 단어가 다르면 0과 재귀 횟수 반환
    elif char[l] != char[r]:
        return 0, cnt
    # 좌표를 서로 하나씩 가깝게 하며 재귀
    else:
        return recursion(char, l + 1, r - 1, cnt + 1)


def isPalindrome(char):
    return recursion(char, 0, len(char) - 1, 1)


for tc in range(1, T + 1):
    print(*isPalindrome(input()))
