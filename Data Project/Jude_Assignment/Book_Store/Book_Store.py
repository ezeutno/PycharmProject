from Jude_Assignment.Book_Store.Book import *

Author_Data = {
    'Test1' : ['test@gmail.com','male'],
    'Test2' : ['test2@gmail.com', 'female']
}
Book_Data = {
    'Gude' : [['Test1','Test2'], 12000, 5],
    'Gude2' : [['Test1','Test2'], 12000, 5],
    'lol' : [['Test1','Test2'], 12000, -1]
}

password = 'TEST1234'
print('Welcome to Book Store')
book_bought = []
book_price = []
while True:
    m = input('Username (MASTER/BUYER) : ')
    if m.upper() == 'BUYER':
        while True:
            print('####################\n________MENU________\n####################')
            print('(1) Buy Books\n(2) Search Book\n(3) Display Book List\n(4) Total Bought \n(5) Exit')
            print('Please input commend!', end=' ')
            x = int(input())


            def repeat_data():
                l = []
                for i in Book_Data.keys():
                    l.append(i)
                return len(l)

            if x == 1:
                print('####################\n________BUY________\n####################')
                if repeat_data() > 0:
                    f = None
                    m = input('Please input book name! ')
                    l_data = Book(0,0,0,0,0,0)
                    for i, j in Book_Data.items():
                        if m.upper() == i.upper():
                            l_data = Book(i, j[0], j[2], j[1], Author_Data, Book_Data)
                            f = l_data.toString()
                            print(f)
                    if f is not None:
                        print('Do you want to buy', m.title(), '?', end =' ')
                        m_choice = input()
                        if m_choice.upper() in ['YES', 'Y']:
                            while True:
                                ask = int(input('How many do you want to buy?'))
                                if ask > 0 :
                                    if l_data.getQty() >= ask :
                                        l_data.setQty(l_data.getQty()-ask)
                                        for i in range(ask):
                                            book_bought.append(l_data.getName())
                                            book_price.append(l_data.getPrice())
                                        break
                                    else :
                                        print('Sorry, We only got ',l_data.getQty())
                            print('You have bought ', set(book_bought),'\nYour total is ', sum(book_price))
                        elif m_choice.upper() in ['NO','N']:
                            continue
                    else :
                        print('Sorry, {0} are out of stock!'.format(m.title()))
                else:
                    print('Sorry, Please contact the seller!')
            elif x == 2:
                print('####################\n______SEARCH______\n####################')
                book_input = input('Please input search data!')
                book_search = []
                count = 0
                for i in Book_Data.keys():
                    for a in book_input.split(' '):
                        if a.upper() in i.upper():
                            count += 1
                    if count >= len(book_input.split(' ')):
                        book_search.append(i)
                    count = 0
                count2 = len(book_search)
                while count2 != 0:
                    if count2 >= 3:
                        print(book_search[-count2], book_search[-(count2-1)], book_search[-(count2-2)])
                        count2 -= 3
                    elif count2 ==2:
                        print(book_search[-count2],book_search[-(count2-1)])
                        count2 -= 2
                    elif count2 == 1:
                        print(book_search[-count2])
                        count2 -= 1
            elif x == 3:
                print('####################\n______DISPLAY______\n####################')
                book_data = []
                for i in Book_Data.keys():
                    book_data.append(i)
                count3 = len(book_data)
                while count3 != 0:
                    if count3 >= 3:
                        print(book_data[-count3], book_data[-(count3 - 1)], book_data[-(count3 - 2)])
                        count3 -= 3
                    elif count3 == 2:
                        print(book_data[-count3], book_data[-(count3 - 1)])
                        count3 -= 2
                    elif count3 == 1:
                        print(book_data[-count3])
                        count3 -= 1
            elif x == 4:
                print('####################\n______TOTAL______\n####################')
                if len(book_bought) != 0:
                    print('You have bought ', set(book_bought), '\nYour total is ', sum(book_price))
                else:
                    print('You haven\'t bought anything')

            elif x == 5:
                print('Thank your for visiting us!')
                book_bought = []
                book_price = []
                break
            else :
                print('Error Input!')
    elif m.upper() == 'MASTER':
        x = input('Password : ')
        if x == password:
            while True:
                print('##########################################')
                print('___________________MENU___________________')
                print('##########################################')
                print('(1) Input Book        (2) Edit Book\n(3) Display Book List (4) Input Author')
                print('(5) Edit Author       (6) Display Author\n(7) Exit')
                print('Please input commend!', end=' ')
                x = int(input())
                if x == 1:
                    print('##########################################')
                    print('__________________INPUT___________________')
                    print('##########################################')
                    list_data = []
                    m_input = input('Please input book name! ')
                    for i in Book_Data.keys():
                        if m_input.upper() == i.upper():
                            list_data.append(i)
                    if len(list_data) == 0:
                        list_author_all = []
                        print('Please input data!')
                        while True:
                            try :
                                m_author_count = int(input('How many author do you want to insert? '))
                                break
                            except :
                                print('Error, Please Try Again')
                        for i in range(m_author_count):
                            m_input_author = input('Please input author ')
                            list_author = []
                            for i in Author_Data.keys():
                                if m_input_author.upper() == i.upper():
                                    list_author.append(i)
                            if len(list_author) == 0:
                                m_email = input('Author email : ')
                                m_gender = input('Author gender : ')
                                Book(m_input,list_author_all,0,0,Author_Data,Book_Data).setAuthor(m_input_author,m_gender,m_email)
                            list_author_all.append(m_input_author)
                        m_price_input = input('What\'s the price off the book? ')
                        print('How many {0} existed? '.format(m_input.title()),end='')
                        m_qty_input = input()
                        Book_Data[m_input.title()] = [list_author_all, m_price_input,m_qty_input]
                    else :
                        print('Book already exist!')
                elif x == 2:
                    print('##########################################')
                    print('___________________EDIT___________________')
                    print('##########################################')
                    input_book = input('Which book do you want to edit? ')
                    l_data = Book(0, 0, 0, 0, 0, 0)
                    for i, j in Book_Data.items():
                        if input_book.upper() == i.upper():
                            l_data = Book(i, j[0], j[2], j[1], Author_Data, Book_Data)
                            f = l_data.toString()
                            print(f)
                    change_book_name = input('Change the book name! ')
                    l_data.setName(change_book_name)
                elif x == 3:
                    print('####################\n______DISPLAY______\n####################')
                    book_data = []
                    for i in Book_Data.keys():
                        book_data.append(i)
                    count3 = len(book_data)
                    while count3 != 0:
                        if count3 >= 3:
                            print(book_data[-count3], book_data[-(count3 - 1)], book_data[-(count3 - 2)])
                            count3 -= 3
                        elif count3 == 2:
                            print(book_data[-count3], book_data[-(count3 - 1)])
                            count3 -= 2
                        elif count3 == 1:
                            print(book_data[-count3])
                            count3 -= 1
                elif x == 4:
                    print('##########################################')
                    print('__________________INPUT___________________')
                    print('##########################################')
                    g_input_author = input('Please input author ')
                    list_author = []
                    for i in Author_Data.keys():
                        if g_input_author.upper() == i.upper():
                            list_author.append(i)
                    if len(list_author) == 0:
                        g_email = input('Author email : ')
                        g_gender = input('Author gender : ')
                        Book(0, 0, 0, 0, Author_Data, Book_Data).setAuthor(g_input_author, g_gender,g_email)
                    else :
                        print(g_input_author.title(), 'already exist!')
                elif x == 5:
                    continue
                elif x == 6:
                    print('##########################################')
                    print('__________________AUTHOR___________________')
                    print('##########################################')
                    author_data = []
                    for i in Author_Data.keys():
                        author_data.append(i)
                    count3 = len(author_data)
                    while count3 != 0:
                        if count3 >= 3:
                            print(author_data[-count3], author_data[-(count3 - 1)], author_data[-(count3 - 2)])
                            count3 -= 3
                        elif count3 == 2:
                            print(author_data[-count3], author_data[-(count3 - 1)])
                            count3 -= 2
                        elif count3 == 1:
                            print(author_data[-count3])
                            count3 -=1
                elif x == 7:
                    break

        else:
            print('Wrong Password!, Please Try Again.')
    else:
        print('Wrong Username!, Please Try Again')
