# 2839. 설탕 배달
N = int(input())
s1, s2 = 3, 5   # 설탕 무게 변수


# 배달 함수 정의
def delivery(n):
    # 설탕이 3kg or 5kg 이면 1 반환
    if n == s1 or n == s2:
        return 1
    # 설탕이 3과 5로 나눠지지 않거나, 해가 아니면 -1 반환
    elif n < s1 or s1 < n < s2 or n == 7:
        return -1
    # 그리디 + 수학(패턴화)
    else:
        # 5로 딱 떨어지면 몫을 반환
        if n % s2 == 0:
            return n // s2
        # 1 남는다 -> 5kg 빼고 3kg 두 개 추가
        elif n % s2 == 1:
            return n // s2 + 1
        # 2 남는다 -> 3kg 4개 채우고 나머지 5kg 채운다
        elif n % s2 == 2:
            return n // s2 + 2
        # 3 남는다 -> 3kg 하나만 추가
        elif n % s2 == 3:
            return n // s2 + 1
        # 4 남는다 -> 3kg 3개 채우고 나머지 5kg 채운다
        else:
            return n // s2 + 2


print(delivery(N))


# 일반적인 그리디 루프
def delivery_2(n):
    cnt = 0     # 자루 갯수 변수
    # 설탕이 남으면 반복
    while n >= 0:
        # 5kg 로 전부 나눠지면 자루 갯수 반환
        if n % 5 == 0:
            return cnt + n // 5
        # 3kg 하나 빼고 자루 갯수 추가한 뒤 반복
        n -= 3
        cnt += 1
    # 나눠지지 않으면 -1 반환
    return -1
