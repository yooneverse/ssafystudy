# BAEK 9358. 순열 접기 게임
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def fold(length, array):    # 배열과 배열 길이를 함수 인자로 받음 
    # 재귀 중단
    if length == 2:         # 배열 길이가 2이면 크기 판단하여 알맞는 값 반환
        if array[0] > array[1]:
            return 'Alice'
        else:
            return 'Bob'


    ceil = length // 2  # 중간값 설정
    a = []              # 수정될 배열 저장할 리스트
    # 반으로 나눠서 반대편 값과 더해줌
    for i in range(ceil):
        a.append(array[i] + array[length - 1 - i])
    # 만약 배열 길이가 홀수라면 중간값 두 배로 새 배열에 저장
    if length % 2 == 1:
        a.append(array[ceil] * 2)
    
    # 재귀 시작
    return fold(len(a), a)


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = fold(N, arr)
    print(f'Case #{tc}: {result}')
