total_items = []
total_price = 0

print("WELCOME TO SHOPPING CART")
while True:
    user_input = input("Enter your item (q to quit): ")
    if user_input == "q" or user_input == "Q":
        break
    else:
        price = float(input(f"Enter the price of {user_input}: "))
        total_items.append(user_input)
        total_price += price
        



print(f"Total price is {total_price}")
