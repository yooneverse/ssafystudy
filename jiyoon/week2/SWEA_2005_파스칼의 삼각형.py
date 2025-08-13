def pascal_triangle(n):
    # r행은 길이 r+1
    tri = [[0] * (r + 1) for r in range(n)]
    tri[0][0] = 1  # 첫 줄은 항상 1
 
    # 왼쪽위(-1,-1), 오른쪽위(-1,0) 두 방향만 사용
    d = [(-1, -1), (-1, 0)]
 
    # 두 번째 줄부터 채우기 (N=1이면 이 반복은 실행되지 않음)
    for r in range(1, n):          # r: 현재 행(1 ~ n-1)
        for c in range(r + 1):     # c: 현재 열(0 ~ r)
            s = 0  # 현재 칸 값의 합
 
            # 현재 칸의 두 부모 좌표 확인 후, 범위 안이면 더하기
            for dr, dc in d:
                pr = r + dr  # 부모 행 (r-1)
                pc = c + dc  # 부모 열
                if (pr >= 0 and pr < r) and (pc >= 0 and pc < r):
                    s += tri[pr][pc]
 
            # 부모가 없으면(가장자리) 1, 있으면 합
            if s > 0:
                tri[r][c] = s
            else:
                tri[r][c] = 1
 
    return tri
 
 
# 출력을 위한 데이터 입력 진행
T = int(input())            # 테스트 케이스 개수
for tc in range(1, T + 1):
    N = int(input())        # 파스칼 삼각형 크기 (1 ≤ N ≤ 10)
    tri = pascal_triangle(N)
 
    print(f"#{tc}")         # 케이스 번호 출력
    for r in range(N):
        print(*tri[r])   