from InfixtoPostfix import main

Answer2 = open('Answer.txt', 'w')
data_operation = main()
stack = []


def push(a):
    stack.append(float(a))


def pop():
    stack.pop()
    stack.pop()


def p4(c):
    pop()
    push(c)


def add(a, b):
    x = float(a) + float(b)
    p4(x)


def minus(a, b):
    x = float(a) - float(b)
    p4(x)


def times(a, b):
    x = float(a) * float(b)
    p4(x)


def div(a, b):
    x = float(a) / float(b)
    p4(x)


def power(a, b):
    x = float(a) ** float(b)
    p4(x)

try :
    for i in data_operation:
        wy = i
        if wy.isnumeric():
            push(wy)
        else:
            if wy == '+':
                add(stack[-2], stack[-1])
            elif wy == '-':
                minus(stack[-2], stack[-1])
            elif wy == '*':
                times(stack[-2], stack[-1])
            elif wy == '/':
                div(stack[-2], stack[-1])
            elif wy == '^':
                power(stack[-2], stack[-1])
    Answer2.write(str(stack[-1]))
except :
    Answer2.write('Error, Please Try Again!\nPlease Check the input in Text.txt')
Answer2.close()
