from Jude_Assignment.Book_Store.Author import *


class Book:
    def __init__(self, name, authors, qty, price, author_data, book_data):
        self.__name = name
        self.__authors = authors
        self.__qty = int(qty)
        self.__price = float(price)
        self.__author_data = author_data
        self.__book_data = book_data

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__book_data[name] = self.__book_data.pop(self.__name)

    def getAuthor(self):
        l = []
        for a in self.__authors:
            for i, j in self.__author_data.items():
                if a == i:
                    data = Author(i, j[0], j[1])
                    l.append(data.toString())
        return l

    def setAuthor(self,name,gender,email):
        Author(name,email,gender).setAuthor(self.__author_data)

    def getPrice(self):
        return self.__price

    def setPrice(self, amt):
        for i, j in self.__book_data.items():
            if self.__name == i:
                j[1] = amt

    def getQty(self):
        return self.__qty

    def setQty(self, amt):
        for i, j in self.__book_data.items():
            if self.__name == i:
                j[2] = amt

    def toString(self):
        Data = Book(self.__name, self.__authors, self.__qty, self.__price, self.__author_data, self.__book_data)
        return "Book[name= {0}, author= {1}, price= {2}, qty= {3}]".format(self.__name, Data.getAuthor(), self.__price,
                                                                        self.__qty)

    def getAuthorNames(self):
        for i, j in self.__book_data.items():
            if self.__name == i:
                return j[0]
