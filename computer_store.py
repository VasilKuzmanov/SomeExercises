net_price, taxes = 0, 0

while True:
    command = input()
    if command in ["special", "regular"]:
        break
    if float(command) < 0:
        print("Invalid price!")
        continue
    net_price += float(command)
    taxes += float(command) * 20 / 100

total_price = net_price + taxes

if command == "special":
    total_price *= 0.9

if net_price != 0:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {net_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$\n-----------\nTotal price: {total_price:.2f}$")
else:
    print("Invalid order!")











