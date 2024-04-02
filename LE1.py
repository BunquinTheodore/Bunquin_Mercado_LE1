game_library = {
    "Donkey Kong": {"quantity": 3, "cost": 2},
    "Super Mario Bros": {"quantity": 5, "cost": 3},
    "Tetris": {"quantity": 2, "cost": 1}  
    }

user_acc = {}
user_inventory = {}

admin_username = "Admin"
admin_password = "adminpass"

def display_available_game():
    print(game_library)
        
def register_user():
    username = input ("Enter your username: ")
    password = input("Enter password: ")
    user_acc[username] = {'Password': password, 'Balance': 0}
    print ("Account Registered Successfully!")
    return

def log_in(username):
    if username in user_acc:
        if log_in_password == user_acc[log_in_name]['Password']:
            logged_in_menu(username)
        else:
            print ("Wrong password")
    else:
        print ("Username not Found")
    
def rent_game(username):
    while True:
        game = input("Game to be rented: ")
        if game in game_library[game] and game_library[game]['quantity'] > 0:
            cost = game_library["cost"]
            if user_acc[username['Balance']]>= cost:
                user_inventory[username] = game
                game_library[game]['quantity'] -= 1
                print (f"{game} Rented Successfully!")
        else:
            print ("No Game Rented")
             

def return_game(username):
    if username in user_inventory:
        game = user_inventory.pop(username)
        game_library[game]['quantity'] += 1
        print (f"{game} returned successfully.")
    else:
        print ("No Game Rented")

def top_up_account(username,amount):
    print("Top-Up")
    while True:
        try:
            print(f"Register User: {register_user}, Balance: {game_library[register_user]['balance']}")
            top_up_amount = float(input("Enter the amount to top-up: "))
            game_library[register_user]['balance'] += top_up_amount
            print("Top-up successsful!")
            print("New Balance: {game_library[register_user]['balance']}")
        except ValueError as e:
            print (f"Error: {e}")
            break


def admin_update_game(game_name):
    if game_name in game_library:
        new_quantity = int(input("Enter new quantity: "))
        new_cost = float(input("Enter new cost: "))
        game_library[game_name]['quantity'] = new_quantity
        game_library[game_name]['cost'] = new_cost
        print(f"{game_name} updated successfully!")
    else:
        print ("Game not found!")

def admin_login():
    username = input ("Enter Admin Username: ")
    password = input ("Enter Admin Password: ")
    if username == admin_username and password == admin_password:
        admin_menu()
    else:
        print ("Invalid Credentials")

def admin_menu():
    print ("Admin Menu")
    print ("1. Add/Update Games")
    choice = int(input("Enter Game to Update: "))
    if choice == 1:
        admin_update_game(game_name)
    else:
        print ("Invalid Choice")

def redeem_free_rental(username):
    pass

def display_game_inventory():
    if username in user_inventory:
        print (f"You have rented game: {user_inventory[username]}")
    else: 
        print ("No  games rented yet.")

def logged_in_menu(username):
    print ("Welcome to Log In Menu!")
    print ("1. Rent a Game")
    print ("2. Return a Game")
    print ("3. Top up Account")
    print ("4. Display Inventory")
    print ("5. Redeem Free-rental")
    print ("6. Log Out")
    choice = input("Enter choice: ")
    if  choice == 1: 
        rent_game(username)
    elif choice == 2:
        return_game(username)
    elif choice == 3:
        top_up_account(username,amount)
    elif choice == 4:
        display_game_inventory()
    elif choice == 5:
        redeem_free_rental(username)
    elif choice == 6:
        print ("Exiting Program...")
        return
        


def check_credentials(username,password):
    if username in user_acc and user_acc[username]["Password"] == password:
        True
    else:
        False


def main():
    while True:
        try:
            print("\n Welcome to the rental Game System")
            print("1. Display Available Game")
            print("2. Register User")
            print("3. Log In")
            print("4. Admin Log In")
            print("5. Exit")
            choice = int(input("Enter your option: "))

            if choice == 1:
                display_available_game()
            elif choice == 2:
                register_user()
            elif choice == 3:
                username = input ("Enter username: ")
                password = input("Enter Password: ")
                check_credentials(username, password)
                if username == admin_username:
                    admin_login()
                else:
                    logged_in_menu(username)
            elif choice == 4:
                admin_login()
            elif choice == 5:
                print ("Exiting Program...")
                break
            else:
                print("Invalid Output. Try another.")
        except ValueError:
            print("Invalid output")

main()




