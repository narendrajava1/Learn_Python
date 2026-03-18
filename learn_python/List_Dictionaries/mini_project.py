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
portfolio = [
    {"stock": "NIFTY", "buy_price": 150, "current_price": 170, "qty": 50},
    {"stock": "BANKNIFTY", "buy_price": 200, "current_price": 180, "qty": 30},
    {"stock": "RELIANCE", "buy_price": 2500, "current_price": 2600, "qty": 10}
]
#calculate profit
total_profit=0
for option_index in portfolio:
    profit=(option_index["current_price"]-option_index["buy_price"])*option_index["qty"]
    print(f"{option_index['stock']} Profit: {profit}")
    total_profit+=profit
    print("Total Profit:", total_profit)