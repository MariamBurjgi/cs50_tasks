menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

order_total = 0.0
while True:
    try:
        item = input("Enter an item: ").title()
    except EOFError:
        # user has pressed control-d, so we break out of the loop
        break

    if item in menu:
        item_price = menu[item]
        order_total += item_price
        print(f"${order_total:.2f}")
    else:
        print("Invalid item")
