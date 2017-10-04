arr = []
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def isNum(num):
    arr2 = list(num)
    for i in range(len(num)):
        if arr2[i] not in nums:
            return False
    return True
def push(num):
    arr.append(float(num))
    print(arr)
def pop():
    return arr.pop()
def add(num1, num2):
    return num1 + num2
def min(num1, num2):
    return num1- num2
def mult(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1/num2
while True:
    try:
        inp = input()
        #print(inp)
        if(inp == '+'):
            num = add(int(pop()), int(pop()))
            push(num)
        elif(inp == '-'):
            num = min(int(pop()), int(pop()))
            push(num)
        elif(inp == '*'):
            num = mult(int(pop()), int(pop()))
            push(num)
        elif(inp == '/'):
            num = div(int(pop()), int(pop()))
            push(num)
        elif(inp == 'exit'):
            break
        else:
            if(isNum(inp)):
                push(inp)
            else:
                print('Error, something went wrong')
    except:
        print('Error, something went wrong')