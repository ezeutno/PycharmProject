def list() :
    a = []
    w = 0
    while w == 0:
        while True:
            x = input("Insert Commands ")
            if x.upper() == 'INSERT':
                y = input("Data ")
                a.append(y)
                print(a)
                break
            elif x.upper() == 'DELETE':
                a.pop(-1)
                print(a)
                break
            elif x.upper() == 'UPDATE':
                z = int(input('The list position '))
                y = input('Data ')
                a.pop(z)
                a.insert(z, y)
                print(a)
                break
            elif x.upper() == 'LIST':
                print(a)
                break
            else:
                print('Error, Please try again!')
        while True:
            c = input('Do you wish to continue? ')
            if c.upper() == 'YES':
                break
            elif c.upper() == 'NO':
                print('Thank you for using inputer')
                w = 1
                break
            else:
                print('Error, Please Try Again!')