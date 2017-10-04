x = input()
y = ['.A', '.O', '.Y', '.I', '.U', '.E']
z = [ ]
count = 0
for i in range(len(x)):
    z.append('.'+x[i])
while count<len(x):
    if z[count].upper() in y :
        z.pop(count)
        count -= 2
    count +=1
print(z)