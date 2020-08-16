input_Data=input("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")



menu = [
    [
        "Wings",
        0
    ],
    [
        "Cookies",
        0
    ],
    [
        "Spring Rolls",
        0
    ],
    [
        "Coffee",
        0
    ],
    [
        "Tea",
        0
    ],
    [
        "Unicorn Tears",
        0
    ],
    [
        "Salmon",
        0
    ],
    [
        "Steak",
        0
    ],
    [
        "Ice Cream",
        0
    ],
    [
        "Cake",
        0
    ],
    [
        "Pie",
        0
    ],
    [
        "A Literal Garden",
        0
    ],    
]


def choose(data):
    for i in range(len(menu)):
        if data == "quit":
            break
        elif data ==menu[i][0]:
            menu[i][1]+=1
            print(f"{menu[i][0]} number of order {menu[i][1]}")
            neworder =input("if you want to order any thing else just type it or you can type quit ")            
            choose(neworder)

    
choose(input_Data)