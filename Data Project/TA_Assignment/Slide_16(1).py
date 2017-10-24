import matplotlib.pyplot as plt
from random import randint
def function(x):
    return x ** 2 - 3 * x + 4
list = [x ** 2 - 3 * x + 4 for x in range(26)]
# Supposed range of x = 25
# x min = 0, x max = 25, y min = 0, y max = 600
x = [randint(0,25) for i in range(4001)]
y = [randint(0,600) for a in range(4001)]

count = 0
total = max(x) * max(y)
plt.plot(x,y, "o", color="red")
plt.plot(list,"o",color='blue')
for i in range(4001):
    if y[i] <= list[x[i]]:
        count+=1

area = count/4000*total
print(area)
plt.show()
