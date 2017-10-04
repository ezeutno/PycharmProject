import Notes.Class
car_2 = Notes.Class.car("Test", "$150.000")
car_2.car_print()

#To import only the function that in it
from Notes.Class import car
car_2 = car("Test", "$150.000")
car_2.car_print()