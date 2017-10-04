spt_onroad = int(input('Time spent on the road = '))
acc = int(input('Acceleration = '))
dis = int(input('Distance = '))
speed_limit = 60


def distance(a):
    return (acc / 2) * (a ** 2)


def speed():
    return acc * spt_onroad


for i in range(spt_onroad+1):
    print("Duration: ", i, 'Distance: ', '*' * int((distance(i) / 10)))
if speed() > speed_limit:
    print('The person went over the speed limit. (Max speed was ', speed(), ' m/s)')
else:
    print('The person did not go over the speed limit. (Max speed was ', speed(), ' m/s)')
if distance(spt_onroad) > dis:
    print('The person reach the destination. (Reached ', distance(spt_onroad), ' m)')
else:
    print('The person did not reach the destination. (Reached ', distance(spt_onroad), ' m)')