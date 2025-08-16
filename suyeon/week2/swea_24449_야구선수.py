T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    players = list(map(int, input().split()))
    players.sort(reverse=True)
 
    max_team = 0
    for i in range(len(players)):
        new_team = 0
        for j in range(i, len(players)):
            if players[i] - players[j] <= k:
                new_team += 1
        if max_team < new_team:
            max_team = new_team
 
    print(f'#{test_case} {max_team}')