import sys
input = sys.stdin.readline

from collections import deque

def conveyor():
    tmp = endurance

    turn = zero = 0
    start = 0
    end = N - 1
    robot = [0] * (2 * N)
    robot_que = deque([])

    # 내구도가 0인 칸이 K이상 이면 종료
    while zero < K:
        turn += 1

        # 벨트가 칸 위에 있는 로봇과 함께 한 칸 회전
        start = (start + (2 * N - 1)) % (2 * N)
        end = (end + (2 * N - 1)) % (2 * N)

        # 가장 먼저 올라간 로봇부터 가능하다면 이동
        while robot_que and robot_que[0][0] != turn:
            _, plate = robot_que.popleft()
            if plate == end:
                robot[plate] = 0
                continue
            next_plate = (plate + 1) % (2 * N)
            if tmp[next_plate] and not robot[next_plate]:
                robot[plate] = 0
                if next_plate != end:
                    robot[next_plate] = 1
                    robot_que.append((turn, next_plate))
                tmp[next_plate] -= 1
                if tmp[next_plate] == 0:
                    zero += 1
            else:
                robot_que.append((turn, plate))

        # 올리는 칸에 로봇 생성
        if tmp[start]:
            robot[start] = 1
            robot_que.append((turn, start))
            tmp[start] -= 1
            if tmp[start] == 0:
                zero += 1
    return turn

N, K = map(int, input().split())
endurance = list(map(int, input().split()))

answer = conveyor()

print(answer)


# import sys
# input = sys.stdin.readline
#
# from collections import deque
#
# def conveyor():
#     turn = zero = 0
#     start = 0
#     end = N - 1
#     robot = [0] * (2 * N)
#     robot_que = deque([])
#
#     # 내구도가 0인 칸이 K이상 이면 종료
#     while zero < K:
#         turn += 1
#
#         # 벨트가 칸 위에 있는 로봇과 함께 한 칸 회전
#         start = (start + (2 * N - 1)) % (2 * N)
#         end = (end + (2 * N - 1)) % (2 * N)
#
#         # 가장 먼저 올라간 로봇부터 가능하다면 이동
#         while robot_que and robot_que[0][0] != turn:
#             _, plate = robot_que.popleft()
#             if plate == end:
#                 robot[plate] = 0
#                 continue
#             next_plate = (plate + 1) % (2 * N)
#             if endurance[next_plate] and not robot[next_plate]:
#                 robot[plate] = 0
#                 if next_plate != end:
#                     robot[next_plate] = 1
#                     robot_que.append((turn, next_plate))
#                 endurance[next_plate] -= 1
#                 if endurance[next_plate] == 0:
#                     zero += 1
#             else:
#                 robot_que.append((turn, plate))
#
#         # 올리는 칸에 로봇 생성
#         if endurance[start]:
#             robot[start] = 1
#             robot_que.append((turn, start))
#             endurance[start] -= 1
#             if endurance[start] == 0:
#                 zero += 1
#     return turn
#
# N, K = map(int, input().split())
# endurance = list(map(int, input().split()))
#
# answer = conveyor()
#
# print(answer)
