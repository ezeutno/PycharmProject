import matplotlib.pyplot as plt

#cube = [x**3 for x in range(3)]
#plt.plot(cube,marker='o')
cube2 = [x**3 for x in range(50)]
numx = [x for x in range(50)]
#plt.plot(numx, cube2,marker='*')
#numx2 = [x for x in range(1000,6000)]
plt.scatter(numx,cube2,c=cube2,cmap=plt.cm.Blues,edgecolors='red',s=40)
plt.show()