stack = []
number =['0','1','2','3','4','5','6','7','8','9']
AC=['AC','ac','Ac','aC']
i=len(stack)
x=0
y=100
wy=0
def push(n):
    stack.append(int(wy))
def pps(n):
    print(x)
    stack.pop(i - 1)
    stack.pop(i - 1)
    stack.append(x)
def add(n):
    x = stack[i-1]+stack[i-2]
    pps(1)
def min(n):
    x=stack[i-1]-stack[i-2]
    pps(1)
def times(n):
    x=stack[i-1]*stack[i-2]
    pps(1)
def div (n):
    x=stack[i-1]/stack[i-2]
    pps()
def pow(n):
    x=stack[i-1]**stack[i-2]
    pps(1)
def modulo(n):
    x=stack[i-1]%stack[i-2]
    pps(1)
while (y == 100):
    try:
        wy = input()
        if(wy=='+'):
            add(1)
            print(stack)
        elif(wy=='-'):
            min(1)
            print(stack)
        elif(wy=='*'):
            times(1)
            print(stack)
        elif (wy=='/'):
            div(1)
            print(stack)
        elif(wy=='**'):
            pow(1)
            print(stack)
        elif(wy=='%'):
            modulo(1)
            print(stack)
        elif (wy[0:1] in number):
            push(1)
            print(stack)
        elif (wy[0:2] in AC):
            stack = []
            print(stack)
    except:
        print("Error, Please Try Again!")