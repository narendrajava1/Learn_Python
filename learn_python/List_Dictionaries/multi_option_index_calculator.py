# ===== CONFIG =====
symbol_config = {
    "NIFTY": {"lot_size": 65, "max_qty": 1755},
    "BANKNIFTY": {"lot_size": 15, "max_qty": 900},
    "SENSEX": {"lot_size": 20, "max_qty": 1000}
}


# ===== FUNCTIONS =====
def calculate_profit(buy_price, sell_price, qty):
    return (sell_price - buy_price) * qty


def calculate_charges(turnover):
    return 40 + (turnover * 0.0008)


def break_even(option_type, strike_price, premium_price):
    return strike_price + premium_price if option_type == "CE" else strike_price - premium_price


# ===== INPUT =====
symbol = input("Enter symbol (e.g., NIFTY 23800 CE): ").upper()

parts = symbol.split()
index = parts[0]
strike = float(parts[1])
option_type = parts[2]

config = symbol_config.get(index)
if not config:
    print("Unsupported index")
    exit()

lot_size = config["lot_size"]
max_qty = config["max_qty"]

lots = int(input("Enter number of lots: "))
qty = lots * lot_size

# ===== ORDER SPLIT =====
orders = []
remaining = qty

while remaining > 0:
    order_qty = min(max_qty, remaining)
    orders.append(order_qty)
    remaining -= order_qty
# ===== PRICE INPUT =====
buy_price = float(input("Enter buy price: "))
sell_price = float(input("Enter current/sell price: "))
stop_loss_price = float(input("Enter stop loss price: "))
# ===== CALCULATIONS =====
total_profit = 0

print("\n--- Order-wise Profit ---")

for i, order_qty in enumerate(orders, 1):
    order_profit = calculate_profit(buy_price, sell_price, order_qty)
    total_profit += order_profit
    print(f"Order {i}: Profit = {order_profit}")

profit = total_profit

total_charges = 0

for order_qty in orders:
    turnover = (buy_price + sell_price) * order_qty
    total_charges += calculate_charges(turnover)

charges = total_charges

net_profit = profit - charges
investment = buy_price * qty
profit_percent = (net_profit / investment) * 100

be = break_even(option_type, strike, buy_price)

# Risk Reward
risk = (buy_price - stop_loss_price) * qty
reward = (sell_price - buy_price) * qty
risk_reward = reward / risk if risk != 0 else 0

return_ratio = net_profit / investment


# ===== OUTPUT =====
print("\n===== TRADE SUMMARY =====")
print("Symbol:", symbol)
print("Lot Size:", lot_size)
print("Lots:", lots)
print("Quantity:", qty)

print("\n--- Order Execution Plan ---")
for i, o in enumerate(orders, 1):
    print(f"Order {i}: {o} qty ({o // lot_size} lots)")

print("\n--- P&L ---")
print("Gross Profit:", round(profit, 2))
print("Charges:", round(charges, 2))
print("Net Profit:", round(net_profit, 2))

print("\n--- Metrics ---")
print("Investment:", investment)
print("Profit %:", round(profit_percent, 2))
print("Break-even:", be)
print("Return Ratio:", round(return_ratio, 4))
print("Risk-Reward Ratio:", round(risk_reward, 2))
