# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3500,
    "MSFT": 300
}

portfolio = {}
total_value = 0

print("Enter your stock holdings (type 'done' to finish):")

while True:
    stock = input("Stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in price list.")
        continue
    try:
        qty = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = qty
    except ValueError:
        print("Please enter a valid quantity.")

# Calculate total investment
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

print(f"\nTotal investment value: ${total_value}")

# Optionally save to file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", 'w') as f:
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
        f.write(f"\nTotal investment value: ${total_value}")
    print("Portfolio saved to 'portfolio_summary.txt'.")
