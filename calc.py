def update_vars(res, last, op, cur):
    if op in '+-':
        res += last
        last = cur if op == '+' else -cur
    # else:
        # last = int(last / cur) if op == '/' else last * cur
    return res, last, 0


def calculate(s):
    stack = []
    res = last = cur = 0
    op = '+'
    le = len(s)
    for i, char in enumerate(s):
        if char.isdigit():
            cur = cur * 10 + int(char)
            if i == le - 1 or not s[i + 1].isdigit():
                res, last, cur = update_vars(res, last, op, cur)
        if char in '+-*/':
            op = char
        if char == '(':
            stack.extend([res, last, op])
            res = last = cur = 0
            op = '+'
        if char == ')':
            cur = res + last
            res, last, op = stack[-3:]
            stack[-3:] = []
            res, last, cur = update_vars(res, last, op, cur)
    return res + last

