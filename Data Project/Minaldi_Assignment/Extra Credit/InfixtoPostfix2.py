def main_run():
    Text_data = open('Text.txt', 'r')
    infix_data = '(' + Text_data.read() + ')'
    post_data = []
    operator_calc = []
    operator = ['(', ')', '+', '-', '*', '/', '^']

    def runtime(a, b):
        if len(operator_calc) != 0:
            while operator_calc[-1] in b:
                post_data.append(operator_calc.pop())
        operator_calc.append(a)

    for i in range(len(infix_data)):
        if infix_data[i].isdigit():
            if i != 0:
                if infix_data[i - 1].isdigit():
                    post_data[-1] = post_data[-1] + infix_data[i]
                else:
                    post_data.append(infix_data[i])
            else:
                post_data.append(infix_data[i])
        elif infix_data[i] in operator:
            m = infix_data[i]
            if m == '(':
                operator_calc.append(infix_data[i])
            elif m == '^':
                runtime(m, ['^'])
            elif m in ['*', '/']:
                runtime(m, ['^', '*', '/'])
            elif m in ['+', '-']:
                runtime(m, ['^', '*', '/', '-', '+'])
            elif m == ')':
                while operator_calc[-1] != '(':
                    post_data.append(operator_calc.pop(-1))
                operator_calc.pop()
    Text_data.close()
    return post_data
