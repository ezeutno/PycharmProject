from Group_Assignment.library import library
from Group_Assignment.List import list

x = input('Please input program type!')
if x.upper()=='LIBRARY':
    library()
elif x.upper()=='LIST':
    list()
