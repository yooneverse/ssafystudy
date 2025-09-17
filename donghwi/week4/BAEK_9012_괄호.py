def VPS():
    result = 'YES'
    for i in range(len(lst)):
        if lst[i] == '(':
            stack.append('(')
        elif stack and lst[i] == ')':
            stack.pop()
        else:
            result = 'NO'
            return result

    if stack:
        result = 'NO'
    else:
        result = 'YES'

    return result


TestCase = int(input())

for _ in range(TestCase):
    lst = list(input())
    stack = []

    print(VPS())
