'''
문제
한 번호가 다른 번호의 접두어인 경우가 있으면 안 됨

50 개 이하 테스트 케이스

전화 번호 수 10,000 개 이하

각 전화 번호 칟대 길이 10

두 전화 번호가 같은 경우는 없음
'''

'''
메모리 초과가 두렵다

공간 복잡도란?
파이썬의 객체는 값뿐만 아니라 객체 타입 정보, 참조 횟수 등 포함하여 메모리 많이 소요

예시
1. num = 911
    - int 객체
    - 숫자 저장 공간 8바이트
    - 오버헤드(타입 정보 등) 20바이트
    - 총 28바이트

2. num = '911'
    - str 객체
    - 9 1 1 세 문자 저장 3바이트
    - 오버헤드: 47바이트 이상
    - 총 50바이트 이상
    
결론
10자리 문자열 100바이트로 가정!!! 
백만 바이트가 1MB 임
이 문제에서는 만 개 번호 있어도 1MB 정도 사용

팁
- 2차원 배열 N x M 크기가 10^5 이상이라면 메모리 초과 의심
- 자료 구조 크기 생각
- 입력 데이터 양 크다면, 모두 저장하지 않고 한 줄씩 읽어서 처리(스트리밍)

'''

import sys
input = sys.stdin.readline

def solve(n):
    phone_book = [input().strip() for _ in range(n)]
    phone_book.sort()

    for i in range(n-1):
        if phone_book[i+1].startswith(phone_book[i]):
            print("NO")
            return

    print("YES")
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    solve(N)

'''
startswith 메서드
문자열이 특정 문자로 시작하는지 확인하여 True 또는 False를 반환

기본 사용 방식
print(phone.startswith("010"))

- 대소문자 엄격 구분


심화 
1. 여러 문자열에도 적용 가능. 소괄호 사용

files = ["test1", "test2", "main"] 

for f in files:
    if f.startswith(("test", "main")):
        print(True)

True
True
True


2. 범위 지정
문자열.startswith(접두어, 시작 인덱스, 끝 인덱스)
        0123456789101112
text = "Hello, Python"
print(text.startswith("Python", 7))         True
print(text.startswith("Python", 7, 10))     False
print(text.startswith("Python", 7, 13))     True (실제 끝인덱스 +1 값)
'''
