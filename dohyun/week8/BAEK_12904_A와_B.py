# BAEK 12904. A와 B
import sys
sys.stdin = open('input.txt', 'r')

# T 마지막 문자가 무엇인지 따라 함수를 적용한다.
# T = ABA -> AB에 A를 추가한 것과 같다.
# T = BBAB -> ABB를 돌리고 B를 추가한 것과 같다.
# 이를 반대로 생각해본다.


# 마지막 문자를 지우고 배열을 거꾸로 돌린다.
def spin(arr):
    arr.pop()
    arr = arr[::-1]
    return arr


# 마지막 문자를 지운다.
def delete(arr):
    arr.pop()
    return arr


# 문자열 슬라이싱을 위해 리스트로 만들어줌
S = []
T = []

for i in input():
    S.append(i)

for i in input():
    T.append(i)


# 만약 T의 길이가 S의 길이보다 크다면 반복
while len(S) < len(T):
    # T의 마지막 문자가 A면 삭제
    if T[-1] == 'A':
        T = delete(T)
    # T의 마지막 문자가 B면 삭제 후 회전
    else:
        T = spin(T)

# 두 배열이 같으면 1, 아니면 0
if S == T:
    print(1)
else:
    print(0)
