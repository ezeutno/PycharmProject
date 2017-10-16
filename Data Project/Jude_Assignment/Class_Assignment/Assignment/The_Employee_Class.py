class Employee:
    def __init__(self,id,firstName,lastName, salary):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def getID(self):
        return self.id

    def getFirstname(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getName(self):
        return self.firstName + self.lastName

    def getSalary(self):
        return self.salary

    def setSalary(self,amt):
        self.salary = amt

    def getAnnualSalary(self):
        return self.salary*12

    def raiseSalary(self, percent):
        self.salary += self.salary*percent/100

    def toString(self):
        return "InvoiceItem[id= {0}, name= {1} {2}, salary= {3}]".format(self.id,self.firstName,self.lastName,self.salary)

