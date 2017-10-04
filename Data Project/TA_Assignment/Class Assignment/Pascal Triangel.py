arr = []
temp =[]
count = 0
pascal = int(input('Please input how many row! = '))
while count <= pascal:
    for i in range (count):
        if (i == 0):
            arr.append (1)
        elif (i == count - 1):
            arr.append (1)
        else:
            x = temp[i] + temp[i-1]
            arr.append(int(x))
    print(arr)
    count +=1
    temp=arr[:]
    arr=[]