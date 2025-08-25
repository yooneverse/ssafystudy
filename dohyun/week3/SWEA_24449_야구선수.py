# 24449. 야구 선수

# 08.20 Stack_2 수업에서 배운 부분집합을 이용함

# 야구선수 팀 만드는 함수 정의
# 인덱스 번호와 팀 내 최대 실력차이를 매개변수로 사용
def baseball(idx, d):
    global max_team  # 전역변수 설정

    # 가지치기: 팀 내 최대 실력차이가 K보다 크면 재귀 중단
    if d > K:
        return

    # 인덱스가 최대이면 인원수도 최대로 잡음
    if idx == N:
        max_team = N
        return

    # 최대 인원수를 저장
    # 여기서 저장하는 이유는 재귀 함수가 돌아가면 가지치기 당하거나
    # 인덱스 값이 최대이면 어차피 이 값이 지워지기 때문
    max_team = max(max_team, len(team))
    # 팀에 넣은 다음 idx 1 증가시키고 팀 내 최대 실력차를 구한 뒤, 재귀 시작
    team.append(player_value[idx])
    baseball(idx + 1, abs(team[0] - team[-1]))
    # 다음 부분집합을 구하기 위해 넣었던 선수 방출
    team.pop()


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    player_value = list(map(int, input().split()))
    # 팀 내 최대 실력차를 구하기 위해 오름차순 정렬
    player_value.sort()
    # 1인 팀이 될 수 있으므로 최대 인원수의 초기 변수 1로 설정
    max_team = 1
    team = []

    # 인덱스가 0인 선수부터 부분집합을 구할 것 / 현재 선수는 한 명이기 때문에 실력차는 없음
    baseball(0, 0)

    print(f'#{tc} {max_team}')
