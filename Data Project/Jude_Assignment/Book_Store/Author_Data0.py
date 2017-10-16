author = {

}

class Author:
    global author
    def __init__(self, name, email, gender):
        self.__name = name.upper()
        self.__email = email
        self.__gender = gender

    def input_author(self):
        author[self.__name][0] = self.__email
        author[self.__name][1] = self.__gender

    def getName(self):
        l = []
        for i in author.keys():
            l.append(i)
        return l

    def getGender(self, name):
        for i,j in author.items():
            if name.upper() == i:
                print(j[1])

    def getEmail(self, name):
        for i,j in author.items():
            if name.upper() == i:
                print(j[0])

    def getFullData(self):
        l = []
        for i,j in author.items():
            l.append("Author[name= {0}, email= {1}, price= {2}]".format(i,j[0],j[1]))
        return l

    def toString(self):
        return '\nName= {0}\nEmail= {1}\nGender= {2}'.format(self.__name,self.__email,self.__gender)