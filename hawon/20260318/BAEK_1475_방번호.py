'''
BAEK_1475_방번호
'''

n = input()

count = [0] * 10

for ch in n:
    num = int(ch)
    count[num] += 1

# 6과 9는 서로 바꿔 쓸 수 있으므로 합쳐서 계산
six_nine = count[6] + count[9]

count[6] = (six_nine + 1) // 2
count[9] = count[6]

print(max(count))