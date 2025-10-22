# 팰린드롬이면 1, 아니면 0
# recur 함수 호출 횟수

# 예제 함수
def recursion(s, l, r):
    global cnt
    cnt +=1
    # 만약 l이 r보다 크거나 같으면-> 1을 리턴
    if l >= r:
        return 1
    # s는 입력받은 문자열 리스트, l이랑 r은 인덱스
    elif s[l] != s[r]:
        return 0
    # l은 시작점이고, r은 끝점이다.
    else:
        return recursion(s, l + 1, r - 1)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)

T = int(input())
for tc in range(1, T+1):
    # 주어진 문자열
    S = list(input().strip())
    cnt = 0
    result = isPalindrome(S)
    print(result,cnt)