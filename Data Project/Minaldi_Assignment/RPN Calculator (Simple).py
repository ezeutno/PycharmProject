stack = []
wy=0
stack.append(int(input()))
stack.append(int(input()))
print(stack)
a=input()
if(a== '+'):
    print(stack[0]+stack[1])
    stack.append(stack[0]+stack[1])
elif(a=='-'):
    print(stack[0]-stack[1])
    stack.append(stack[0]-stack[1])
elif(a=='*'):
    print(stack[0]*stack[1])
    stack.append(stack[0]+stack[1])
elif(a=='/'):
    print(stack[0]/stack[1])
    stack.append(stack[0]/stack[1])
elif(a=='**'):
    print(stack[0]**stack[1])
    stack.append(stack[0]**stack[1])
stack.pop(0)
stack.pop(0)
print (stack)
