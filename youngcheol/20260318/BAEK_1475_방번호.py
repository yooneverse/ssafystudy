# 한세트에 0번에서 9번까지 숫자 하나

# 방 번호가 주어졌을때 필요한 세트의 개수의 최솟값
# 6이랑 9는 뒤집어서 사용가능(임마 때문에 머리아픔)

N = input()

count = [] * 10

for num in N:
    #꺼낸 문자가 6이나 9일 경우
    if num == '6' or num == '9':
        count[6] += 1
    else:
        count[int(num)] += 1

# 6과 9의 필요 세트 수 계산 (올림)
count[6] = (count[6] + 1) // 2

# 배열 중 최댓값이 필요한 세트의 최솟값
print(max(count))