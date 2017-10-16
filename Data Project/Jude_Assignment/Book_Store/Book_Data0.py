from Jude_Assignment.Book_Store.Author_Data0 import *
book = {

}

class Book:
    m = author(0,0,0)
    def __init__(self, name, authors, qty, price):
        self.__name = name
        self.__authors = authors
        self.__qty = int(qty)
        self.__price = float(price)

    def getName(self):
        book_data = []
        for i in book:
            book_data.append(i)
        

    def getAuthor(self):
        return self.__authors

    def getPrice(self):
        return self.__price

    def setPrice(self, amt):
        self.__price = amt

    def getQty(self):
        return self.__qty

    def setQty(self, amt):
        self.__qty = amt

    def book_input(self):
        book[self.__name][0] = self.__authors
        book[self.__name][1] = self.__qty
        book[self.__name][2] = self.__price


    def toString(self):
        global m
        return "Book[name= {0}, authors{{1}},price= {2}, qty= {3}]".format(self.__name,m.getFullData(),self.__price,self.__qty)

    def getAuthorsName_Book(self):
        global m
        z = []
        for i in m.getName():
            z.append(i)
        return z

    def getAuthorsNames_All(self):
        global m
        for i in m.getFullData:
            return i, ' '

    def Data(self):
        return book
