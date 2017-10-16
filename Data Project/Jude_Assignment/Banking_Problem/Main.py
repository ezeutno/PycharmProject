from Bank import Bank
from Customer import Customer

display = {
    'MENU' : ['Log in','Create New Customer','Display All Customer','EXIT'],
    'CUSTOMER MENU' : ['Get Customer Info','Add Account','Display All Account','Account Login','EXIT'],
    'ACCOUNT MENU' : ['Get Balance','Withdraw','Deposit','EXIT']
}

data_all = [['176501009',['Hans','Tunprem'],[['ACC001','50000']]]]

def display_output(menu_type):
    x = int((22 - len(menu_type)) / 2)
    print('\n', '-' * x, menu_type.upper(), '-' * x)
    for i,j in display.items():
        if menu_type.upper() == i:
            for a in range(len(j)):
                print('[{0}] {1}'.format(a+1,j[a]))
    print('#'*(x*2+len(menu_type)+3))

def display_account(username,b):
    if b == 1:
        for i in data_all:
            if username == i[0]:
                for a in i[-1]:
                    count = 1
                    print('[{0}] {1}'.format(count,a[0]))
                    count += 1
                if len(i[-1]) == 0:
                    print('NONE')
    if b == 0:
        for i in data_all:
            if username == i[0]:
                for a in i[-1]:
                    count = 1
                    print('[{0}] {1}, Balance Rp. {2}.'.format(count,a[0],a[1]))
                    count += 1
                if len(i[-1]) == 0:
                    print('NONE')

def buffer_zone():
    input('Press enter to continue! ')

while True:
    try:
        display_output('MENU')
        x = input('Please input command!')
        if x == '1':
            display_output('Login')
            u_input = input('Input customer username! ')
            for i in data_all:
                if u_input == i[0]:
                    while True:
                        z = Customer(i[1][0], i[1][1],0,0)
                        display_output('Customer Menu')
                        d = input('Please Input command!')
                        if d == '1':
                            print('First Name : ', z.getFirstName())
                            print('Last Name : ', z.getLastName())
                            print('All Account')
                            display_account(u_input,0)
                        elif d == '2':
                            display_output('Add Account')
                            x = input('Account Name: ')
                            print('Your Account Name is : {0}'.format(z.newAccount(x,i[-1])))
                        elif d == '3':
                            display_output('Display All Account')
                            display_account(u_input,1)
                        elif d == '4':
                            a_input = int(input('Which Account to Login?'))
                            while True:
                                display_output('Account Menu')
                                x = input('Please input command!')
                                z = Customer(i[1][0],i[1][1],i[-1][a_input-1][0],i[-1][a_input-1][1])
                                if x == '1':
                                    display_output('Get Balance')
                                    print(z.getBalance())
                                elif x == '2':
                                    display_output('Withdraw')
                                    w_input = int(input('How many do you want to withdraw? '))
                                    i[-1][a_input-1][1] = z.withdraw(w_input)
                                elif x == '3':
                                    display_output('Deposit')
                                    d_input = int(input('How many do you want to deposit? '))
                                    i[-1][a_input-1][1] = z.deposit(d_input)
                                elif x == 4:
                                    break
                                else :
                                    print('Wrong Input!')
                                buffer_zone()
                        elif d == '5':
                            break
                        else:
                            print('Wrong Input!')
                        buffer_zone()
        elif x == '2':
            display_output('Create New Customer')
            z = Bank(data_all,len(data_all),'Bank')
            print(z.addCustomer(input('Please input first name! '),input('Please input last name! ')))
            buffer_zone()
        elif x == '3':
            display_output('Display All Customer')
            z = Bank(data_all, len(data_all), 'Bank')
            print('The Total number of customer is {0}'.format(str(z.getNumOfCustomers())))
            for i in range (z.getNumOfCustomers()):
                print('[{0}] {1}'.format(i+1,z.getCustomers(i)))
            buffer_zone()
        else :
            break
    except:
        print('Error,Please Try Again!')
