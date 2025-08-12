# 알고리즘 수업 - 버블 정렬 3
# 시간초과가 나는데 시간을 줄일 수 있는 방법이 혹시 뭐가 있을까요

# 버블 정렬 함수 정의
def bubble_sort(sort_arr, compare_arr, arr_len):
    if sort_arr == compare_arr:
        return 1

    for i in range(arr_len - 1, 0, -1):
        for j in range(i):
            if sort_arr[j] > sort_arr[j+1]:
                sort_arr[j], sort_arr[j+1] = sort_arr[j+1], sort_arr[j]
            # 바꾸고 난 후, 두 리스트가 동일한지 비교
            if sort_arr == compare_arr:
                return 1
    return 0


# 입력 받기
n = int(input())  # A, B의 크기
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

print(bubble_sort(arr_a, arr_b, n))
