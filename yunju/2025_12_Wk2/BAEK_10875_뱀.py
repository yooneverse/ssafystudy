'''
그냥 냅다 풀면 메모리 초과 뜸 ㅠㅠ
why? 맵의 사이즈가 (2L+1) (2L+1)
0 <= L <= 10^8 (1억)
즉 맵의 크기가 2억 * 2억 을 넘어감 (4경?!)


아이디어

뱀이 죽는 경우
1. 맵을 벗어날 때
2. 본인의 몸통과 만날 때

뱀의 이동 방식
1. 가로 or 세로
2. 90도 회전

방향 전환하는 지점을 알아내고
해당 지점이 맵을 벗어나지 않는지 판단
이동 선분이 과거 이동했던 선분과 교차하는지 확인
(가로선과 세로선)

'''

'''
주의점

과거 선분들과 교차여부 판정 시
가장 가까운 (먼저 만나는) 선분을 기준으로 판단해야 함

직전 선분의 끝점과 출발점 겹치므로 비교 대상에서 직전 선분 제외

'''

'''
고려하지 못한 점
가로선이 세로선이 아닌 가로선과 만날 수 있다
언제? 출발점
'''
import sys
input = sys.stdin.readline

def solve():
        ans = 0
        # 방향 (오른 아래 왼 위)
        dir_num = 0
        dx = (1,0,-1,0)
        dy = (0,1,0,-1)

        L = int(input())
        # 시작 지점
        cx = cy = L

        row = [] # (출발x, 도착x, y)
        col = [] # (출발y, 도착y, x)

        turn_cnt = int(input())
        for i in range(turn_cnt):
            command = input().split()
            second = int(command[0])
            dir = command[1]

            # i가 짝수라면 가로선, 홀수라면 세로선
            if (i%2) == 0:
                nx = cx + dx[dir_num]*second
                ny = cy

                # 본인의 몸통과 만나는 경우 죽음
                # 새로운 직선의 두 x 좌표 사이에 세로선 x좌표 있고
                # 새로운 직선의 y 좌표가 세로선 두 y좌표 사이에 있는 경우
                # 출발점이 직전 끝점과 같은 경우는 제외
                if col:
                    # 교차 가능 선분 중 최소 거리
                    min_dist = float('inf')
                    for start_y, arrive_y, xx in col[:len(col)-1]:

                        if (cx <= xx <= nx) or (nx <= xx <= cx):
                            if (start_y <= cy <= arrive_y) or (arrive_y <= cy <= start_y):
                                min_dist = min(min_dist, abs(cx-xx))

                    # (L,L)과 만날 가능성 추가
                    if cy == L:
                        if (cx <= L <= nx) or (nx <= L <= cx):
                            min_dist = min(min_dist, abs(L-cx))

                    if min_dist != float('inf'):
                        return ans + min_dist

                # 맵을 벗어나면 죽음
                if nx<0:
                    return ans + cx + 1
                if nx>2*L:
                    return ans + (2*L+1-cx)

                # 가로선 추가
                row.append((cx,nx,cy))
                # 위치 변경
                cx = nx
                cy = ny

            else:
                nx = cx
                ny = cy + dy[dir_num]*second

                if row:
                    min_dist = float('inf')
                    for start_x, arrive_x, yy in row[:len(row)-1]:

                        if (cy <= yy <= ny) or (ny <= yy <= cy):
                            if (start_x <= cx <= arrive_x) or (arrive_x <= cx <= start_x):
                                min_dist = min(min_dist, abs(yy-cy))
                    if min_dist != float('inf'):
                        return ans + min_dist

                # 맵을 벗어나면 죽음
                if ny < 0:
                    return ans + cy + 1
                if ny > 2 * L:
                    return ans + (2 * L + 1 - cy)

                # 세로선 추가
                col.append((cy, ny, cx))
                # 위치 변경
                cx = nx
                cy = ny

            # 죽지 않았다
            # 시간 추가
            # 이동 끝난 후 방향 전환
            ans += second

            if dir == 'L':
                dir_num += 3
                dir_num %= 4

            else:
                dir_num += 1
                dir_num %= 4
        # 회전이 종료
        # 해당 방향으로 계속 가나?
        if dir_num == 0:
            wall_dist = 2 * L - cx
            min_dist = wall_dist+1

            if col:
                for start_y, arrive_y, xx in col:
                    if cx < xx <= 2 * L and (start_y <= cy <= arrive_y or arrive_y <= cy <= start_y):
                        min_dist = min(min_dist, xx - cx)

                if cy == L:
                    if cx <= L:
                        min_dist = min(min_dist, abs(L - cx))
            ans += min_dist

        elif dir_num == 1:
            wall_dist = 2 * L - cy
            min_dist = wall_dist+1
            if row:
                for start_x, arrive_x, yy in row:
                    if cy < yy <= 2 * L and (start_x <= cx <= arrive_x or arrive_x <= cx <= start_x):
                        min_dist = min(min_dist, yy - cy)
            ans += min_dist

        elif dir_num == 2:
            wall_dist = cx
            min_dist = wall_dist+1
            if col:
                for start_y, arrive_y, xx in col:
                    if 0 <= xx < cx and (start_y <= cy <= arrive_y or arrive_y <= cy <= start_y):
                        min_dist = min(min_dist, cx - xx)
                if cy == L:
                    if L <= cx:
                        min_dist = min(min_dist, abs(L-cx))
            ans += min_dist

        else:
            wall_dist = cy
            min_dist = wall_dist+1
            if row:
                for start_x, arrive_x, yy in row:
                    if 0 <= yy < cy and (start_x <= cx <= arrive_x or arrive_x <= cx <= start_x):
                        min_dist = min(min_dist, cy - yy)
            ans += min_dist

        return ans

print(solve())
