class Author:
    def __init__(self, name, email, gender):
        self.__name = name
        self.__gender = gender
        self.__email = email

    def getAuthor(self):
        return [self.__name,self.__email,self.__gender]

    def setAuthor(self,author):
        author[self.__name] = [self.__email, self.__gender]

    def toString(self):
        return "Author[name= {0}, email= {1}, gender= {2}]".format(self.__name,self.__email,self.__gender)