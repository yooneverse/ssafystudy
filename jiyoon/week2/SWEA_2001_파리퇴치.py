T = int(input()) # 테스트 케이스 개수
 
for tc in range(1, T+1): # 각 케이스 순회
    N, M = map(int, input().split()) # 띄어쓰기 있는 정수 값 받아오기
    matrix = [list(map(int, input().split())) for _ in range(N)] # 리스트를 2차원 배열로 만들기, 안 내용은 다 정수
     
    max_fly = 0 # 최대값 초기화
     
    for i in range(N-M+1): #행 순회
        for j in range(N-M+1): # 열 순회
            total = 0 # 잡은 수 초기화
             
            for r in range(i, i+M): #M만큼 범위로 탐색
                for c in range(j, j+M): #M만큼 범위로 탐색
                    total += matrix[r][c] #탐색한 범위 내 숫자 잡은 수에 합산
                     
                    if max_fly < total:
                        max_fly = total #최댓값 갱신
                         
    print(f"#{tc} {max_fly}")