t = int(input())

for _ in range(t):
    ew = input()
    length = len(ew) - 1

    # 패턴이 유효한지 확인하는 변수
    answer = True

    # 0: 100+1+, 1:01, 3:None
    case = 3
    # 패턴에서 연속되는 0과 1의 개수
    one = 0
    zero = 0

    # 문자열 뒤에서부터 패턴 확인
    for i in range(length, -1, -1):
        if ew[i] == '1':
            # zero > 1 -> case == 0인 경우
            # 100+1+에서 앞부분 1은 한 개 이므로 패턴 종료
            if zero > 1:
                case = 3
                zero = 0
                continue

            # 01이 완성되었으므로 변수 초기화
            if one == 1 and zero == 1:
                one = 0
                zero = 0

            # 1011+의 형태이므로 패턴이 아님
            elif one > 1 and zero == 1:
                answer = False
                break

            one += 1

            # 1이 1개인 경우에 case 변경
            if one == 1:
                case = 1
        # 0인 경우
        else:
            # case == 0 -> 00+1+인 경우
            if not case:
                pass
            # 1없이 0이 먼저 나온 경우 패턴이 아님
            elif not one:
                answer = False
                break

            zero += 1

            # 00+1+인 경우 1개수 초기화 및 case 변경
            if zero > 1:
                case = 0
                one = 0

    # 패턴이 완성되지 않고 반복문이 종료된 경우
    # 01패턴으로 반복문이 종료된 경우 case 변환이 없으므로
    # 이 경우를 제외하고 answer 변경
    if not(case == 3):
        if case == 1 and one == 1 and zero == 1:
            pass
        else:
            answer = False

    if answer:
        print('YES')
    else:
        print('NO')
