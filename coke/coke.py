def main():
    price = 50
    print("Amount Due: " + str(price))

    coin = calculate()
    print("Change Owed: " + str(abs(coin)))


def calculate():
    price = 50
    total_amount = 0

    while total_amount < price:
        amount = int(input("Insert Coin: "))
        if amount == 25 or amount == 10 or amount == 5:
            total_amount += amount
            print("Amount Due: " + str(price - total_amount))
        else:
            print("Amount Due: " + str(price - total_amount))


    coin = total_amount - price
    return coin

main()

