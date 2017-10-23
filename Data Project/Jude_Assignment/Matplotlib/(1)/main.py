import matplotlib.pyplot as plt

#cube in a range of 3
cube = [x**3 for x in range(3)]
plt.plot(cube,marker='o')
#cube in a range of 50
cube2 = [x**3 for x in range(5000)]
numx = [x for x in range(5000)]
plt.plot(numx, cube2,marker='*')
#cube in scatter a range of 5000 plot in 1000 - 6000
numx2 = [x for x in range(1000,6000)]
plt.scatter(numx2,cube2,c=cube2,cmap=plt.cm.Blues,edgecolors='none',s=40)
plt.show()