x = [1,1,1,1,1,2]
if x.__contains__(1):
    y = int(x.count(1))
    for i in range(y):
        x.remove(1)
print(x)