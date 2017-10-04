def main():
    Text_data = open('Text.txt','r')
    infix_data = '('+Text_data.read()+')'
    post_data = []
    operator_calc = []
    operator = ['(',')','+','-','*','/','^']
    count = 0
    while count != len(infix_data):
        if infix_data[count].isdigit():
            if count != 0:
                if infix_data[count-1].isdigit():
                    x = post_data[len(post_data) -1][0:]+infix_data[count]
                    post_data.pop()
                    post_data.append(x)
                else :
                    post_data.append(infix_data[count])
            else :
                post_data.append(infix_data[count])
        elif infix_data[count] in operator:
            m = infix_data[count]
            if m == '(':
                operator_calc.append(infix_data[count])
            elif m == '^':
                operator_calc.append(m)
            elif m in ['*', '/']:
                if len(operator_calc) != 0:
                    while operator_calc[len(operator_calc)-1] in ['^','*', '/']:
                        post_data.append(operator_calc[len(operator_calc)-1])
                        operator_calc.pop()
                operator_calc.append(m)
            elif m in ['+', '-']:
                if len(operator_calc) != 0:
                    while operator_calc[len(operator_calc)-1] in ['^', '*', '/', '-', '+']:
                        post_data.append(operator_calc[len(operator_calc)-1])
                        operator_calc.pop()
                operator_calc.append(m)
            elif m == ')':
                while operator_calc[-1] != '(':
                    post_data.append(operator_calc.pop(-1))
                operator_calc.pop()
        count += 1
    Text_data.close()
    return post_data

