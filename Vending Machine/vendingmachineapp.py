'''
================================================

Intro to Programming
Assessment 2: Vending Machine (Utility App)

Name: Kelvin Bautista
Student ID: 04-24-164
Instructor: Ms. Lavanya

================================================
'''

## Importing the necessary modules for my vending machine

import sqlite3 # Importing sqlite3 to use a database for my vending machine menu
import os # Importing os to make a 'clear terminal' function for clean outputs
import tabulate # Importing tabulate to make a clean and organized table format for my vending machine menu
import time # Importing time to add delays and loading animations

## Clear Terminal
# This function clears the terminal screen. I only added this because I think it makes my output cleaner.

def ct():

    # os.system() comes from the os module, which allows Python to interact with the operating system.

    os.system('cls' if os.name == 'nt' else 'clear') # This runs a command that clears the terminal based on the type of operating system you have.
    # The 'cls' command clears the terminal for Windows, while 'clear' does the same for Unix-like systems such as Linux or macOS.

## Loading message template
# Since this is a vending machine, I figured adding a loading message animation would be a fun little detail.

def loading_msg(message): # Added a message parameter here so that I can reuse it for different strings throughout the whole program.
    for e in range(2): # This starts a for loop that runs two times.
        print(f"{message}.", end="\r") # This prints a message but instead of adding a new line, it overwrites the same line with \r.
        time.sleep(0.5) # A delay effect that pauses the program for 0.5 seconds.
        print(f"{message}..", end="\r")
        time.sleep(0.5)
        print(f"{message}...", end="\r") 
        time.sleep(0.5)

## SQLite3 Database Connection
# For my vending machine menu, I will be using an sqlite3 database.

con = sqlite3.connect('menu.db') # This command connects the program to the sqlite3 database I made which is named 'menu'.
c = con.cursor() # Here, I'll be using c as a cursor to execute SQL commands.

## Wallet
# This is for the user's spending to buy items from the vending machine. The user will first start off with 1,000.

user_wallet = 1000.00

'''

]] ==================== [1] VENDING MACHINE ==================== [[

'''

## Show Menu
# Shows the vending machine menu

def show_menu():
    c.execute("SELECT * FROM vm_menu ORDER BY id;") # Selects all rows from the vm_menu table and orders them by ID
    all_items = c.fetchall() # Fetches all those rows and stores them in all_items variable

    table = [] # This is to prepare an empty list to store the table data

    for record in all_items: # Loops through each row in all_items
        
        id, item, price, stock, category = record # Sets each field into individual variables

        table.append([id, item, f"¥{price:.2f}", stock, category]) # Adds the data to the empty table list (Price is formatted with a yen symbol and two decimal places)

    headers = ["ID", "Item", "Price", "Stock", "Category"] # Adds header names that match each field

    # Using the tabulate command, we made a table for the menu:

    menu = tabulate.tabulate(table, headers=headers, tablefmt="grid") # Combining the table list, header names, and grid format together, we got ourselves an organized menu.

    print("\nKyoByte [キョ] Menu:") # Prints title of vending machine
    print()
    print(menu)

## Select item
# This function selects items in the vending machine. Made this a function so that I could reuse it throughout the whole program.

def select_item(item_id):
    qry = "SELECT * from vm_menu WHERE id = ?" # The query that selects all data from the vm_menu table is stored in the 'qry' variable.
    c.execute(qry, (item_id,)) # Executes the query with 'item_id' as the parameter to replace the '?' placeholder.
    selected_item = c.fetchone() # Fetches the row that came from the query result.
    return selected_item # Returns the result.

## Update stock
# This function updates the stock in the database.

def update_stock(item_id, quantity):
    qry = "UPDATE vm_menu SET stock = stock - ? WHERE id = ?" # Updates the database by setting an item's stock to a certain value.
    c.execute(qry, (quantity, item_id)) # Executes the query with 'item_id' and 'quantity' as the parameters to replace the two '?' placeholders.
    con.commit() # Commits the changes in the database

## Handling the quantity of items
# I made it so that the user can buy multiple quantities of the same item. If the user goes beyond the stock limit, it automatically adjusts to 50 which is the maximum capacity.

def ask_for_quantity(item_name, stock):

    while True: # A while loop to keep asking until the loop is broken.

        try:
            quantity = int(input(f"How many {item_name} would you like to buy? (Available stock: {stock}): ")) # Asks for user's input on how many items they want.

            # Go back

            if quantity == 0: # If user's input is 0, this returns 0 which goes back a previous step.
                return 0

            # Adjusting purchase if beyond stock limit

            if quantity > stock: # If user's input goes beyond stock limit, it tells the user to try again.
                print(f"Only {stock} {item_name} are available. Please try again.")

            # Negative stock

            elif quantity < 0: # If user's input is below 0, user must try again.
                print("Invalid quantity. It must be a positive value.")

            else:
                return quantity # Quantity is returned.

        except ValueError: # If user does not type a valid number, they are prompted to try again.
            print("Invalid input. Please enter a valid number.")

## Handling user's payment
# This function handles the user's payment with a change system.

def payment(total):
    global user_wallet # Since this is global, I can access the user_wallet variable even if it is inside this function.

    if total > user_wallet: # If the total is way higher than the user's wallet amount then it returns None which resets the cycle.
        print()
        print(f"Insufficient funds. Your total is ¥{total:.2f}, but your wallet balance is only ¥{user_wallet:.2f}. Please try again.")
        return 0, 0 # This returns 0 which resets the process for the user.
    
    while True:

        try:
            print()
            print(f"[金] Your total is ¥{total:.2f}.")
            print(f"[金] Your current wallet balance is ¥{user_wallet:.2f}")
            print()

            user_paid_amount = float(input("[=] Please enter the amount you'd like to pay: ")) # User input asking how much they want to pay.

            if user_paid_amount == 0: # If input is 0, 0 is returned to make the user go back a previous step.
                return 0, 0
                                     
            if user_paid_amount > user_wallet: # If user tries to input an amount that goes way beyond their wallet amount, it asks again.
                print(f"Insufficient funds. Your balance is ¥{user_wallet:.2f}.")

            elif user_paid_amount < total: # If user inputs an amount lower than the total, it asks again.
                print(f"Insufficient amount. You need at least ¥{total:.2f} to purchase this item.")

            else: # If user inputs a reasonable amount, the commands below are ran:

                change = user_paid_amount - total # Change is calculated by subtracting the user's amount paid with the total price.
                user_wallet -= user_paid_amount # User wallet is subtracted by the amount the user paid.
                user_wallet = user_wallet + change # User wallet receives change.

                if change > 0: # If change is above 0, it runs a loading animation and lets the user know their change.
                    message = "Processing payment"
                    loading_msg(message) # Using the loading_msg function, the message stored in the 'message' variable is passed.

                    print()
                    print(f"Payment successful! Your change is ¥{change:.2f}.")

                else: # If there's no change, it runs these commands below instead:
                    message = "Processing payment"
                    loading_msg(message)

                    print()
                    print("Payment successful!")

                print(f"Your new wallet balance is ¥{user_wallet:.2f}.") # Lets the user know their new wallet balance.
                return user_paid_amount, change # Returns the user's amount paid and change.
            
        except ValueError: # If user inputs an invalid amount, it asks again.
            print("Invalid input. Please enter a valid amount.")

## Print receipt
# Added this function to let the user know the details of their order.

def print_receipt(item_name, price, quantity, total, user_paid_amount, change):

    # Loading animation

    message = "Printing receipt"
    loading_msg(message)

    # Receipt title

    print()
    print("=== Receipt ===")
    print()

    # A list is created to hold the details of the purchase. Each detail is paired with their corresponding value.

    receipt_data = [
        ["Item", item_name], # (e.g Item, Coca Cola)
        ["Price", f"¥{price:.2f}"],
        ["Quantity", quantity],
        ["Total", f"¥{total:.2f}"],
        ["Amount Paid", f"¥{user_paid_amount:.2f}"],
        ["Change", f"¥{change:.2f}"]
    ]

    # Here, the receipt_data list is formatted into a table-like layout using fancy_grid. It is then stored in the receipt variable.

    receipt = (tabulate.tabulate(receipt_data, tablefmt="fancy_grid"))
    print(receipt) # Receipt variable is printed.
    print("================")
    print()

## Purchase item
# The purchase item feature in the vending machine. This is where the magic happens.

def purchase_item():

    ct() # Clears the terminal for a cleaner output.

    show_menu() # Shows menu.

    while True:
        try:

            print()
            print("[自] Please type the item ID for the product you'd like to buy. (Type '0' to go back)")
            item_id = int(input("Item ID: ")) # User input asking for item ID.

            # Selecting item

            item = select_item(item_id) # After receiving the item ID, it passes it to the select_item() function to select that specific item in the database.

            # Checking item

            if item_id == 0: # If item_id is 0, it returns to main() which represents going back a previous step.
                ct()
                main()
                return

            if not item: # If user inputs an ID that isn't in the menu, it tells them that it does not exist.
                print()
                print("Item ID does not exist.")
                continue

            item_name, price, stock = item[1], item[2], item[3] # Extracts items from item list and assigns them to these variables.

            # Check stock

            if stock <= 0: # If item's stock is below or equal to 0, it asks again.
                print(f"Sorry, {item_name} is out of stock. Please try again.")
                continue
            
            # Else, it runs these commands below:

            print()
            print(f"You have selected {item_name} - ¥{price:.2f}.")
            print(f"Your current balance is ¥{user_wallet:.2f}.")
            print()

            # Handling the quantity of items a user wants
            
            quantity = ask_for_quantity(item_name, stock) # Calls the quantity handling function

            if quantity == 0: # If the quantity function returns 0, it goes back to item selection to reset steps.
                continue

            total = price * quantity # Price is multiplied by the quantity of items the user picked. It is then stored in the total variable.

            # Handling user's payment

            user_paid_amount, change = payment(total)  # The returned values from the payment function is assigned to these two variables.

            if user_paid_amount == 0: # If this is 0, it returns to item selection to reset steps.
                continue

            # Delay to see change

            time.sleep(10)

            # Loading animation
            
            message = "Hang tight! Your item is being dispensed now"
            loading_msg(message)
            ct() # Clears terminal for a cleaner output.

            print()
            print(f"Thank you! Enjoy your {item_name}!")
            print()

            # Giving the receipt to the user.

            while True:
                print()
                ask_receipt = input("Would you like the receipt? (Y/N): ") # Asking for user's input whether or not they want the receipt.
                ask_receipt = ask_receipt.upper() # Capitalizes the user's input to ensure no errors.

                if ask_receipt == "Y":
                    print_receipt(item_name, price, quantity, total, user_paid_amount, change) # Using all the stored variables with data, it is passed to this functiont to print a receipt.
                    break # Breaks loop
        
                elif ask_receipt == "N": # If user says N, it breaks the loop and moves on.
                    print("Alright!")
                    break

                else: # If user types in something invalid, it asks again.
                    print("Invalid input. Please type Y or N.")

            # Update stock after user's purchase

            update_stock(item_id, quantity) # This function updates the stock based on the quantity of items the user has purchased.

            break # Breaks loop

        except ValueError: # If user inputs an invalid item ID, it asks again.
            print("Invalid input. Please enter a valid ID.")

## Vending Machine
# The vending machine program itself with a little retry feature.

def vending_machine():
    while True:
        purchase_item() # Calls the purchase_item function
        
        retry = input("[自] Would you like to buy another item? (Y/N): ") # Asks the user if they wanna try again.
        if retry.upper() == 'Y': # If user's response is Y, it continues the loop.
            continue
        elif retry.upper() == 'N': # If user's response is N, it breaks the loop.
            break
    
    print("[終] Thank you for using our vending machine! Sayonara!")

    time.sleep(2) # Delay to pause the program.

    ct()

'''

]] ==================== [2] TOP UP WALLET ==================== [[

'''

## Adding balance
# If the user wants to add more to their wallet, this feature helps them out.

def add_balance():
    global user_wallet # Since this is global, I can access the user_wallet variable even if it is inside this function.

    ct() # Clears terminal.

    while True:
        try:
            print()
            print(f"[金] You currently have ¥{user_wallet:.2f} in your wallet. (Type 0 to go back.)")

            # Asking user input

            print()
            top_up = float(input("Please enter the amount you'd like to load into your wallet: ")) # Asks how much they want to put into their wallet.

            if top_up < 0: # If user types a negative value, it asks again.
                print("Please enter a positive amount.")
                continue

            elif top_up == 0: # If user types 0, it returns a previous step which returns to the main screen.
                ct()
                main()
                break
            
            # Adding to user wallet

            user_wallet += top_up # User wallet is added by the top up amount the user typed.

            # Loading animation

            message = f"Adding ¥{top_up:.2f} to your balance"
            loading_msg(message)
            ct()

            # Lets the user know how much they have now.

            print(f"[金] Successfully added ¥{top_up:.2f} to your wallet.")
            print()
            print(f"[金] Your new wallet balance is: ¥{user_wallet:.2f}")
            break

        except ValueError: # Asks again if given an invalid input.
            print("Invalid input. Please enter a valid amount.")

## Asking to add balance again
# This is to ask the user if they wanna add to their balance again.

def add_balance_again():

    while True:
        print()
        retry_balance = input("Would you like to top up again? (Y/N): ") # User input to ask if the user wants to top up again.
        retry_balance = retry_balance.upper() # Capitalizes the user's input to ensure no errors.

        if retry_balance == "Y":
            add_balance() # Calls the add_balance() function again.

        elif retry_balance == "N":
            ct()
            break

        else:
            print("Invalid input. Please type Y or N.")

'''

]] ==================== [3] ADMIN MODE ==================== [[

'''

## Restock item
# This function gives the user the ability to restock a single item from the menu.

def restock_item():

    ct()
    show_menu()

    while True:
        try:
            print()

            item_id = int(input("[保] Enter the ID of the item you want to restock: ")) # Asks the user what item they wanna restock based on the item ID.

            # Select stock

            c.execute("SELECT stock FROM vm_menu WHERE id = ?", (item_id,)) # A query that selects the stock of the item based on the item ID given.
            current_stock = c.fetchone() # Fetches the result of the query.

            if item_id == 0: # If input is 0, it returns a previous step which returns to the admin_mode menu.
                admin_mode()
                return

            if not current_stock: # If item ID does not exist, it asks again.
                print("Item ID not found.")
                continue

            current_stock = current_stock[0] # Gets the stock value from the fetched result.

            # Select item

            c.execute("SELECT item FROM vm_menu WHERE id = ?", (item_id,)) # A query that selects an item based on the item ID given.
            item_name = c.fetchone() # Fetches the result of the query.
            item_name = item_name[0] # Gets the item name from the fetched result.


            while True:
                try: 
                    print()
                    print(f"[保] Current stock of item {item_name}: {current_stock}.")
                    restock_quantity = int(input("How much would you like to add? : ")) # Asks how much they want to add to the stock.

                    if restock_quantity == 0: # If input is 0, it returns a previous step which returns to the admin_mode menu.
                        ct()
                        admin_mode()

                    if restock_quantity < 0: # If input is negative, it asks again.
                        print("Invalid quantity. Please enter a positive number.")
                        continue

                    # Adding to stock

                    new_stock = current_stock + restock_quantity # Else, user's given input is added to the current stock amount of the item.

                    if new_stock > 50: # If user's given input exceeds 50, it adjusts the amount to 50 as 50 is the set maximum capacity for the stock.
                        new_stock = 50

                    # Updating database

                    c.execute("UPDATE vm_menu SET stock = ? WHERE id = ?", (new_stock, item_id)) # A query that sets an item's stock to a certain value.
                    con.commit() # Commits the database changes.

                    # Loading animation

                    print()
                    message = "Restocking"
                    loading_msg(message)
                    ct()

                    # Printed message to tell the user that item has been restocked.

                    print(f"[保] Successfully restocked item {item_name}.")
                
                    return

                except ValueError: # If user has given an invalid input, it asks again.
                    print("Invalid input. Please enter a valid number.")

        except ValueError:
            print("Invalid input. Please enter a valid item ID.")

## Restock again
# This is to ask the user if they wanna restock an item again.

def restock_again():

    while True:
        print()
        retry_restock = input("[保] Would you like to restock again? (Y/N): ") # User input that asks the user if they wanna restock again.
        retry_restock = retry_restock.upper() # Capitalizes user input to ensure no errors.

        if retry_restock == "Y":
            restock_item() # Calls restock_item() function again.

        elif retry_restock == "N":
            ct()
            break
        else:
            print("Invalid input. Please type Y or N.")

## Restock all items
# This is to restock the whole menu.

def restock_all():
    ct()

    # Loading animation

    message = "Restocking all items"
    loading_msg(message)

    ct()

    # Updating the database

    c.execute("UPDATE vm_menu SET stock = 50") # A query that updates every item's stock in the menu to 50 (maximum capacity).
    con.commit() # Commits database changes.
    
    print("[保] All items have been restocked.")

    time.sleep(2) # Delay to pause the program.

## Update price
# This gives the user the ability to update an item's price.

def update_price():

    ct()
    show_menu()

    while True:
        try:
            print()
            item_id = int(input("[実] Please enter the ID of the item whose price you want to update: ")) # Asks user for item ID
            item = select_item(item_id) # Selects item from the database.

            if item_id == 0: # If user input is 0, it returns a previous step which goes back to the admin_mode menu.
                admin_mode()
                return

            if not item: # If item ID does not exist, it prints this message and asks again.
                print("Item ID does not exist. Please try again.")
                continue

            item_name, current_price = item[1], item[2] # Extracts items from item list and assigns them to these variables.

            print()
            print(f"[実] You have selected {item_name}. Current price is ¥{current_price:.2f}.")
            

            while True:
                try:
                    
                    new_price = float(input(f"Enter the new price for {item_name}: ")) # Asks the user to enter new price for the item.

                    if new_price == 0: # If the user types 0, it resets and goes back to admin_mode menu.
                        ct()
                        admin_mode()
                        return

                    if new_price < 0: # If input is negative, it asks again.
                        print("Price cannot be negative. Please try again.")

                    else: # Else, it updates the price.
                        qry = "UPDATE vm_menu SET price = ? WHERE id = ?"
                        c.execute(qry, (new_price, item_id)) # Query sets the price to new_price based on the item ID.
                        con.commit() # Commits database changes.

                        # Loading animation

                        print()
                        message = "Updating item price"
                        loading_msg(message)

                        # Printed message to let the user know.

                        print()
                        print(f"[実] {item_name} price updated successfully to ¥{new_price:.2f}.")

                        break

                except ValueError: # If given an invalid input, it asks again.
                    print()
                    print("Invalid input. Please enter a valid number.")

            break

        except ValueError: # If given an invalid input, it asks again.
            print("Invalid input. Please enter a valid number.")

## Update price again
# This is to ask the user if they wanna update the price of an item again.

def update_price_again():

    while True:
        print()
        retry_price = input("[開] Would you like to update the price of an item again? (Y/N): ") # User input asking if they wanna update the price of an item again.
        retry_price = retry_price.upper() # Capitalizes user's input to ensure no errors.

        if retry_price == "Y":
            update_price() # Calls update_price() function again.

        elif retry_price == "N":
            ct()
            break
        else:
            print("Invalid input. Please type Y or N.")

## Admin Mode
# This is the admin mode menu. This is where the user can configure the vending machine.

def admin_mode():
    ct()

    # Menu screen for Admin Mode

    print('''
==================================================================================

        [道] Welcome to Admin Mode! You can now configure the vending machine.
            Please select a number from the following to proceed:
          
                            [1] Restock item
                            [2] Restock all items
                            [3] Update item price
                            [0] Go back
          
==================================================================================
''')

    # Choosing an option
    
    while True:
        try:
            user_answer = int(input("Please choose an option: "))

            if user_answer == 1: # If user types 1, they can restock an item in the menu.
                restock_item()
                restock_again()
                break
                
            elif user_answer == 2: # If user types 2, they can restock the whole menu.
                restock_all()
                break

            elif user_answer == 3: # If user types 3, they can update the price of an item.
                update_price()
                update_price_again()
                break

            elif user_answer == 0: # If user types 0, they return to the main menu.
                ct()
                main()
                break

            else: # If the user types anything else, it asks again.
                print("Invalid option. Please choose between 1 and 3.")

        except ValueError: # If user gives invalid input, it asks again.
            print("Invalid input. Please choose between 1 and 3.")


'''

]] ==================== [X] MAIN UI ==================== [[

'''

## Main UI
# Decided to make the main UI separate to keep the main function clean and organized.

def main_ui():
    print('''
=========================================================================

        Konnichiwa! Welcome to KyoByte [キョ] Vending Machine!
                Select a number from the following:
          
                        [1] Purchase Item
                        [2] Top Up Wallet
                        [3] Admin Mode
                        [0] Exit
          
=========================================================================
''')

## Main
# The main branch that connects all features through a menu.

def main():

    ct()
    main_ui() # Shows main UI screen

    while True:
        
        try:

            # Choosing an option
            
            print()
            user_input = int(input("Pick an option: "))

            if user_input == 1: # If user types 1, they can use the vending machine.
                vending_machine()
                main_ui()
                
            elif user_input == 2: # If user types 2, they can add to their wallet.
                add_balance()
                add_balance_again()
                main_ui()
                
            elif user_input == 3: # If user types 3, they can configure the vending machine.
                admin_mode()
                main_ui()
                
            elif user_input == 0: # If user types 0, they close the program.
                ct()
                print("Sayonara!")
                exit()

            else: # If user types anything else, it asks again.
                print()
                print("Invalid input. Please choose between 1 and 3.")
        
        except ValueError: # If user gives invalid input, it asks again.
            print("Invalid input. Please choose between 1 and 3.")


main() # This calls the main function.
