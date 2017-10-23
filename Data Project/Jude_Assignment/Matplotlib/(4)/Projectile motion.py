import math
import matplotlib.pyplot as plt

while True:
    try:
        x = input('How many trajectories? ')
        all_legend = []
        for i in range(int(x)):
            y = int(input('Enter initial velocity for trajectory {0} (m/s): '.format(i+1)))
            z = int(input('Enter the angle of projection for trajectory {0} (degrees): '.format(i+1)))
            z_sin = round(math.sin(math.radians(z)),15)
            z_cos = round(math.cos(math.radians(z)),15)
            g = 10
            t = (2*y*z_sin)/g
            all_dis = []
            all_height = []
            for a in range(int(t*1000)):
                dis = z_cos*y*(a/1000)
                height = (y*z_sin*(a/1000))-((1/2)*g*((a/1000)**2))
                all_dis.append(dis)
                all_height.append(height)
            all_legend.append('[{0}*,{1}]'.format(z,y))
            plt.plot(all_dis,all_height)
        plt.legend(all_legend)
        plt.title('Projectile Motion')
        plt.xlabel('Distance (m)')
        plt.ylabel('Height (m)')
        plt.show()
        break
    except:
        print('Error, Please Try Again!')
