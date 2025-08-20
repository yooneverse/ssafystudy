# 알고리즘 수업- 버블 정렬 2
def bubble_sort(arr, arr_len, limit):
    count = 0
    for i in range(arr_len - 1, 0, -1):
        for j in range(i):
            # 요소를 오름차순으로 바꾸면서, counting하고 k와 비교합니다.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
                if count == limit:
                    return arr
    return -1


n, k = map(int, input().split())
num_list = list(map(int, input().split()))

result = bubble_sort(num_list, n, k)

# 함수 return 값에 따라 출력을 다르게 했습니다.
if result != -1:
    for i in result:
        print(i, end=' ')
else:
    print(result)
