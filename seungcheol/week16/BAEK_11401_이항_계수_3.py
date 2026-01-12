n, k = map(int, input().split())

p = 13#1000000007
upper_num = 1
lower_num = 1
left_num = 1
right_num = 1
upper_e = 0
lower_e = 0
for i in range(1, n + 1):
    upper_e += (upper_num * i) // p
    upper_num = (upper_num * i) % p

    if i <= k:
        left_num = (left_num * i) % p
    if i <= n - k:
        right_num = (right_num * i) % p
    if right_num * left_num > p:
        lower_e += (right_num * left_num) // p
        left_num = (right_num * left_num) % p
        right_num = 1

print(upper_num)
print(upper_e)
print(left_num)
print(right_num)
print(lower_e)
answer = upper_num // (left_num * right_num) + (upper_e - lower_e) * p // (left_num * right_num)
print(answer)
