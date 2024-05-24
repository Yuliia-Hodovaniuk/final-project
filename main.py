import admin
import customer


def admin_menu():
    while True:
        print("Welcome to Admin Menu")
        print("1. Login")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1': 
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if admin.Admin.validate_login(username, password):
                admin.clients_menu() 
            else:
                print("Incorrect username or password.")
                
        elif choice == '2':
            print("Exiting admin menu...")
            break
        else:
            print("Error, please choose 1 or 2")


def customer_menu():
    while True:
        print("Welcome to Customer Menu")
        print("1. Login")
        print("2. Sign in")
        print("3. Exit")
        print("Please enter your choice")
        
        customer_choice = input()
        
        if customer_choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            
            if customer.Customer.validate_login(username, password):
               print(customer.spange_bob_menu()) 
            else:
                print("Incorrect username or password.")
                        
        elif customer_choice == "2":
            first_and_last_name = input("Enter your First and Last name: ")
            date_of_birth = input("Enter your date of birth: ")
            address = input("Enter your address: ")
            phone_number = input("Enter your phone number: ")
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            new_customer = customer.Customer(first_and_last_name, date_of_birth, address, phone_number, username, password)
            upload_documents = int(input("How many documents would you like to upload? "))
            for i in range(upload_documents):
                document = input(f"Enter document {i+1}: ")
                new_customer.upload_document(document)
            print("Thank you for joining BARAKUDA Bank! Your registration is under review. We'll get back to you shortly to confirm your new account.")
            break

        elif customer_choice == "3":
            print("Exiting customer menu...")
            break
        
        else:
            print("Error, please choose 1, 2, or 3.")

def main_menu():
    print("Welcome to BARRACUDA bank!")
    
    while True:
        print("Main Menu")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        print("Please enter your choice")

        choice = input()
        if choice == "1":
            customer_menu()  
        elif choice == "2":
            admin_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Error, please choose 1, 2, or 3.")


if __name__ == "__main__":
    main_menu()