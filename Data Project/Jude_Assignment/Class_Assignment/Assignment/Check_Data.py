from Jude_Assignment.Class_Assignment.The_InvoiceItem_Class import InvoiceItem
from Jude_Assignment.Class_Assignment.The_Account_Class import *

m = InvoiceItem(1231234,'Peap',34,12000)
print(m.getID())
m.setUnitPrice(1500000)
print(m.getUnitPrice())
print(m.getTotal())
print(m.toString())

