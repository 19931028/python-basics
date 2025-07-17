
# Vending Machine flow control

items = {
    "1": ("Water", 5.00),
    "2": ("Gatorade", 7.50),
    "3": ("Diet Coke", 6.50),
    "4": ("Sprite", 6.50),
    "5": ("Monster", 8.00)
}
print("Welcome to the Vending Machine!")
print("Select an item NOW!")
# Display menu
def show_menu():
    print("\nMenu Items:")
    for key, (name, price) in items.items():
        print(f"{key}. {name} - ${price:.2f}")
# Start with user funds
user_funds = float(input("\nInsert money to start ( 5.00): $"))
# Main purchase loop
while True:
    show_menu()
    payment_method = input("\nChoose payment method (cash or card): ").lower()
    if payment_method not in ["cash", "card"]:
        print("Invalid payment method.")
        continue
    choice = input("Enter the number of the item you want: ")
    if choice in items:
        item_name, item_price = items[choice]
        print(f"You selected: {item_name} (${item_price:.2f})")
        # Check if user has enough money
        if user_funds >= item_price:
            print("Dispensing item...")
            user_funds -= item_price
            print(f"{item_name} dispensed. Remaining funds: ${user_funds:.2f}")
        else:
            print("Sorry, not enough funds.")
    else:
        print("Item not found, please select another.")
    # Ask if user wants to buy again
    again = input("\nWould you like to buy more? (yes/no): ").lower()
    if again != "yes":
        print("Have a nice day!")
        break