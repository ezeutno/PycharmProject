x = input().upper()
z = ['X']


def a():
    if len(z) == 1:
        z.insert(0, '')
    elif len(z) == 2:
        z.pop(0)
#change the first and the second cup

def b():
    if len(z) == 2:
        z.insert(0, '')
    elif len(z) == 3:
        z.pop(0)
#change the second and the third cup

def c():
    if len(z) == 1:
        z.insert(0, '')
        z.insert(0, '')
    elif len(z) == 3:
        z.pop(0)
        z.pop(0)
#change the first and the third cup

for i in range(len(x)):
    if (x[i] == 'A'):
        a()
    elif (x[i] == 'B'):
        b()
    elif x[i] == 'C':
        c()
print(len(z))
