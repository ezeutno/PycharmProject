import matplotlib.pyplot as plt
from random import randint

list = [x**2-3*x+4 for x in range(26)]
count = 0
for _ in range (4000):
    x = randint(0,25)
    y = randint(0,600)
    plt.plot(x,y,'o',color='green')
    if y <= list[x]:
        count+=1
plt.plot(list,'o',color = 'red')
area = 600*25*count/4000
print(area)
plt.show()