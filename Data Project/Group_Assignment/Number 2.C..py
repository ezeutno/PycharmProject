price_list = {
    "FOODS" : {"CHICKEN":5 , "POTATO": 3, "RICE":3},
    "BAVERAGES" : {"COCA-COLA":2, "PEPSI":1, "Fanta":2},
    "FROZEN-GOODS" : {"ICE-CREAM":4, "YOGURT":5, "JELLY":3},
    "FRUITS" : {"APPLE":10,"PIER":13, "PEACH":14}
}
def calc(x) :
    for i,j in price_list.items():
        y = 0
        if i == x.upper():
            for k,n in j.items():
                print(k, end = " ")
                y = y + n
            print("$",y,"\n")
print("Welcome to Lotte Mart")
while True:
    print("What would you like to buy?")
    print("1. Foods, 2. Beverages, 3. Frozen-GOODS, 4. Fruits")
    x = input()
    if x.upper() not in price_list.keys():
        print('Wrong Input \n')
    else :
        calc(x)
        break