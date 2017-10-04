list = [5,75,15,20,8,9,10,23,45,50,152]

def maximum(x):
    max1 = x [0]
    for i in range (len(x)):
        if max1 <= x[i]:
            max1 = x[i]
    return max1

print(maximum(list))
