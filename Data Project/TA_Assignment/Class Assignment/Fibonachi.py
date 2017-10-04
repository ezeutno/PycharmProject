z = []
for i in range (2):
    x = input('Please input the number! = ')
    z.append(int(x))
y=0
while y<=100:
    y = z[-1] + z[-2]
    print (y)
    z.append(y)