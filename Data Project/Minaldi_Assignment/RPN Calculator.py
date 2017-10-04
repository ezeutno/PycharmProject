stack = []


def push(a):
    stack.append(int(a))


def pop():
    stack.pop()
    stack.pop()


def p4(c):
    print(c)
    pop()
    push(c)
    print(stack)


def add(a, b):
    x = a + b
    p4(x)


def minus(a, b):
    x = a - b
    p4(x)


def times(a, b):
    x = a * b
    p4(x)


def div(a, b):
    x = a / b
    p4(x)


def power(a, b):
    x = a ** b
    p4(x)


def modulo(a, b):
    x = a % b
    p4(x)


print('This is a RPN Calculator\nPlease input an operator or number!')
while True:
    wy = input()
    if wy.isnumeric():
        push(wy)
        print(stack)
    elif wy.upper() == 'AC':
        stack = []
        print(stack)
    elif wy.upper() == "OFF":
        break
    elif len(stack) > 1:
        if wy == '+':
            add(stack[-1], stack[-2])
        elif wy == '-':
            minus(stack[-1], stack[-2])
        elif wy == '*':
            times(stack[-1], stack[-2])
        elif wy == '/':
            if stack[-2] != 0:
                div(stack[-1], stack[-2])
            else:
                print('Error, Please Try Again!')
                while True:
                    yn = str(input('Do you wish to continue the list? '))
                    if yn.upper() == "YES":
                        break
                    elif yn.upper() == "NO":
                        stack = []
                        break
                    else:
                        print('Error, Please Try Again!')
                print(stack)
        elif wy == '**':
            power(stack[-1], stack[-2])
        elif wy == '%':
            modulo(stack[-1], stack[-2])
    else:
        print('Error, Please Try again!')
        while True:
            yn = str(input('Do you wish to continue the list? '))
            if yn.upper() == "YES":
                break
            elif yn.upper() == "NO":
                stack = []
                break
            else:
                print('Error, Please Try Again!')
        print(stack)
print('The last value of your calculation is ', stack, "\nThank you for using Simple Calculator")