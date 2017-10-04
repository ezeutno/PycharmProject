def myfact(x):
    if x == 1:
        return 1
    else:
        y = x * myfact(x - 1)
    return y


print(myfact(int(input())))
