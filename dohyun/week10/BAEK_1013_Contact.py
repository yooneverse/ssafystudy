# BAEK 1013. Contack
import sys, re
sys.stdin = open('input.txt', 'r')

# for tc in range(int(input())):
#     string = input()
#
#     def is_valid(s):
#         a = len(s)
#         i = 0
#         while i < a:
#             if s[i] == '0':
#                 if a - i < 2 or s[i + 1] == '0':
#                     return False
#                 i += 2
#             else:
#                 if a - i < 3 or s[i + 1] == '1' or s[i + 2] == '1':
#                     return False
#                 i += 3
#                 while i < a and s[i] == '0':
#                     i += 1
#
#                 idx = 0
#
#                 while i < a and s[i] == '1':
#                     i += 1
#                     idx += 1
#
#                 if idx == 0:
#                     return False
#
#         return True
#
#     if is_valid(string):
#         print('YES')
#     else:
#         print('NO')


pattern = re.compile(r'^(100+1+|01)+$')

T = int(input())
for _ in range(T):
    s = input()
    print("YES" if pattern.fullmatch(s) else "NO")