def library():
    book_title = input('Book Title:')
    person_name = input('Your Name:')
    print('Hello, are you going to :\n1. Borrow\n2. Return\n3. Read here\n(input "1" or "2" or "3")')
    choice = input()
    if int(choice)==1:
        print('Successfully Borrowed:\n')
        print(book_title , person_name)
    elif int(choice)==3:
        print('Please read inside the library')
        print(book_title, person_name)
    elif int(choice)==2:
        book_day = input("Today's Day: ")
        book_month = input("Today's Month: ")
        print("thank you for borrowing!")
        print(book_title , person_name)
    else:
        print('ERROR!!! NOT WITHIN RANGE')
