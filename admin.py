import logging

logging.basicConfig(level=logging.INFO)

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def validate_login(username, password):
        if username == "admin" and password == "1111":
            return True
        else:
            return False

class Clients:
    customers = {
        "Spange Bob": {
            "first_and_last_name": "Spange Bob",
            "date_of_birth": "01.01.2000",
            "address": "Bikini Bottom",
            "phone_number": "1234",
            "password": "1111"
        }
    }

    @staticmethod
    def create_customer(first_and_last_name, date_of_birth, address, phone_number, username, password):
        if username in Clients.customers:
            return f"Customer with username {username} already exists!"
        Clients.customers[username] = {
            "first_and_last_name": first_and_last_name,
            "date_of_birth": date_of_birth,
            "address": address,
            "phone_number": phone_number,
            "password": password
        }
        return f"Customer {first_and_last_name} created successfully!"
    
    @staticmethod
    def update_customer(username, new_address=None, new_phone_number=None):
        if username in Clients.customers:
            if new_address:
                Clients.customers[username]["address"] = new_address
            if new_phone_number:
                Clients.customers[username]["phone_number"] = new_phone_number
            return f"Customer {username} updated successfully!"
        else:
            return "Customer not found."

    @staticmethod
    def delete_customer(username):
        if username in Clients.customers:
            del Clients.customers[username]
            return f"Customer {username} deleted successfully!"
        else:
            return "Customer not found."

def clients_menu():
    while True:
        print("Welcome back Admin")
        print("1. Create customer")
        print("2. Update customer")
        print("3. Delete customer")
        print("4. Exit")
        print("Please enter your choice:")
        
        choice = input("Enter your choice (1, 2, 3, or 4): ")
        
        if choice == '1':
            first_and_last_name = input("Enter first and last name: ")
            date_of_birth = input("Enter date of birth: ")
            address = input("Enter address: ")
            phone_number = input("Enter phone number: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(Clients.create_customer(first_and_last_name, date_of_birth, address, phone_number, username, password))
        
        elif choice == '2':
            username = input("Enter username of customer to update: ")
            new_address = input("Enter new address (leave blank to skip): ")
            new_phone_number = input("Enter new phone number (leave blank to skip): ")
            print(Clients.update_customer(username, new_address if new_address else None, new_phone_number if new_phone_number else None))
        
        elif choice == '3':
            username = input("Enter username of customer to delete: ")
            print(Clients.delete_customer(username))
        
        elif choice == '4':
            print("Exiting admin menu...")
            break
        
        else:
            print("Error, please choose 1, 2, 3, or 4")

def admin_menu():
    while True:
        print("Welcome to Admin Menu")
        print("1. Login")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if Admin.validate_login(username, password):
                clients_menu()
            else:
                print("Incorrect username or password.")
                
        elif choice == '2':
            print("Exiting admin menu...")
            break
        else:
            print("Error, please choose 1 or 2")
