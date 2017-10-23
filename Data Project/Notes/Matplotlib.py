import matplotlib.pyplot as plt

#first
squares = [1,4,9,16,25,35,49]
plt.plot(squares, marker='o')
plt.title("Squares")
plt.xlabel('x coordinate')
plt.ylabel('y coordinate')
plt.show()

#second
squares_2 = [1,4,9,16,25]
numx = [1,3,5,7,9]
numy = [2,4,6,8,10]

plt.plot(squares_2,marker='o')
plt.plot(numx,numy,marker='*')
plt.title("Series of Number")
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")

plt.legend(['squares 2','nums and many'])
plt.show()

#third
numx = list(range(1,1001))
numy = [x**2 for x in numx]
plt.scatter(numx,numy,c=numy,cmap=plt.cm.Blues ,edgecolor = 'none',s=40)
plt.axis([0,1100,0,1100000])
plt.show()
