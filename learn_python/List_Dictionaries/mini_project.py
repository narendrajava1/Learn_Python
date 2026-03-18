# 🚀 Mini Project: Stock Portfolio Profit Calculator
# 🎯 Goal
#
# You will:
#
# Store stock data using list + dictionary
#
# Calculate investment & profit
#
# Print a simple report
stock=input("Enter stock symbol: ")
buy_price=float(input("Enter buy price: "))
qty=int(input("Enter quantity: "))
current_price=float(input("Enter current price: "))
portfolio = [
    {"stock": stock, "buy_price": buy_price, "current_price": current_price, "qty": qty}
]
#calculate profit
total_profit=0
for option_index in portfolio:
    profit=(option_index["current_price"]-option_index["buy_price"])*option_index["qty"]
    print(f"{option_index['stock']} Profit: {profit}")
    total_profit+=profit
    print("Total Profit:", total_profit)

# 🔥 Step 4: Improve (Add Investment Calculation)
total_investment = 0

for item in portfolio:
    investment = item["buy_price"] * item["qty"]
    total_investment += investment

print("Total Investment:", total_investment)
# 🔥 Step 5: Profit % (Advanced)
profit_percent = (total_profit / total_investment) * 100
print("Profit %:", profit_percent.__round__(2))