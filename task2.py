
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stock_prices:

    price = stock_prices[stock_name]
    total_value = price * quantity

    print("\n----- Stock Portfolio Summary -----")
    print("Stock Name :", stock_name)
    print("Stock Price:", price)
    print("Quantity   :", quantity)
    print("Total Investment Value =", total_value)

    file = open("portfolio.txt", "w")

    file.write("----- Stock Portfolio Summary -----\n")
    file.write(f"Stock Name : {stock_name}\n")
    file.write(f"Stock Price: {price}\n")
    file.write(f"Quantity   : {quantity}\n")
    file.write(f"Total Investment Value = {total_value}\n")

    file.close()

    print("\nData saved successfully in portfolio.txt")

else:
    print("Stock not found in dictionary!")
