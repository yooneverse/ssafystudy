# [S/W 문제해결 기본] 1일차 - Flatten
# 최고점과 최저점의 간격을 줄이는 작업을 평탄화
# 최고점 최저점 차이가 최대 1 이내 (0~1)
# 가로 길이, 상자 높이는 100 이내
# 덤프는 1 이상 1000 이하

T = 10
for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))

    for i in range(N):
    # 최고점과 최저점을 구해야 함
        max_val = 0
        max_idx = -1
        min_val = 101 # 상자 높이는 100 이내이므로
        min_idx = -1

        for k in range(len(box)):
            if max_val < box[k]:
                max_val = box[k]
                max_idx = k
            if min_val > box[k]:
                min_val = box[k]
                min_idx = k

        box[max_idx] -= 1
        box[min_idx] += 1

# 근데, 이렇게 빼다보면 최댓값이랑 최솟값이 바뀜
# 최댓값 최솟값 다시 구하기

    max_val = 0
    min_val = 101 # 상자 높이는 100 이내이므로

    for j in range(len(box)):
        if max_val < box[j]:
            max_val = box[j]
        if min_val > box[j]:
            min_val = box[j]

    print(max_val-min_val)