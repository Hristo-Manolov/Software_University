budget = float(input())
extras = int(input())
clothing = float(input())

decor = budget * 0.1

if extras > 150:
    clothing -= clothing * 0.1

total_price = decor + (extras * clothing)

if total_price <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total_price - budget:.2f} leva more.")

