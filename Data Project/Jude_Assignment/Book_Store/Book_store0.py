from Jude_Assignment.Book_Store.Book_Data0 import *
m = book(0,0,0,0)
password = 'TEST'
print('Welcome to Book Store')
while True:
    m = input('Username (MASTER/BUYER) : ')
    if m.upper() == 'BUYER':
        l = []
        for i in m.Data().keys:
            l.append(i)
        if len(l) == 0:
            print('Sorry, We are out off stock!')
        else :
            for i in
    elif m.upper() == 'MASTER':
        x = input('Password : ')
        if x == password :

