T = int(input()) # 테스트 케이스 입력
 
for tc in range(1, T+1):
    N, K = map(int, input().split()) # 띄어쓰기 있는 정수 값
    arr = list(map(int, input().split())) #순회를 위해 리스트로 입력받음
     
    # 최댓값 기준으로만 해서 최댓값이 포함되지 않는 경우를 빠트림
    # 부분집합 개념으로 해서 최댓값이 없어도 구간이 생길 수 있음을 포괄해야 함
     
    arr.sort()  # 정렬 안 하면 구간을 제대로 못 잡음
     
    max_team = 0  # 최대 팀 크기 저장
     
    # i번째 선수를 구간의 최댓값으로 본다
    for i in range(N):
        max_member = arr[i]
        total_member = 0  # 이번 구간에서 몇 명 들어가는지 세는 변수
         
        # i에서부터 왼쪽으로 확인하면서 조건 맞는 선수 세기
        for j in range(i, -1, -1):
            if max_member - arr[j] <= K:  # 차이가 K 이하라면 팀에 넣기
                total_member += 1
            else:
                break  # 정렬돼 있으니까 여기서 끊으면 됨
         
        # 지금까지 나온 팀 크기 중 제일 큰 값으로 갱신
        if total_member > max_team:
            max_team = total_member
     
    # 최종 결과 출력
    print(f"#{tc} {max_team}")
