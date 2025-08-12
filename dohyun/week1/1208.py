# def bubble_sort(a, n):  # 버블 정렬 함수 생성
#     for i in range(n-1, 0, -1):
#         for j in range(i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a


def counting_sort(data, k=100):  # 카운팅 정렬 함수 생성
    counts = [0] * (k+1)
    temp = [0] * len(data)

    for i in range(len(data)):
        counts[data[i]] += 1

    for i in range(1, k+1):
        counts[i] += counts[i-1]

    for i in range(len(data)-1, -1, -1):
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]

    return temp


for test_case in range(1, 11):  # 테스트 케이스: 10
    dump_count = int(input())   # 덤프 횟수 입력
    height = list(map(int, input().split()))
    sorted_height = counting_sort(height)   # 상자 높이 오름차순으로 정렬

    for dump in range(dump_count):  # 덤프 횟수만큼 반복
        sorted_height[0] += 1   # 가장 작은 상자의 높이 + 1
        sorted_height[-1] -= 1  # 가장 높은 상자의 높이 - 1
        bub_sorted_height = counting_sort(
            sorted_height, len(sorted_height))  # 다시 오름차순으로 정렬
        sorted_height = bub_sorted_height   # 반복하기 위해 재할당

    # 가장 높은 상자와 가장 낮은 상자의 높이 차 계산
    print(f'#{test_case} {sorted_height[-1] - sorted_height[0]}')
