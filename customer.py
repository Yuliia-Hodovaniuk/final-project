import logging

logging.basicConfig(level=logging.INFO)

class Customer:
    def __init__(self, first_and_last_name, date_of_birth, address, phone_number, username=None, password=None):
        self.name = first_and_last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.balance = 1000 
        self.documents = []
        
    def upload_document(self, document):
        self.documents.append(document)
        logging.info(f"Document uploaded for customer {self.name}: {document}")

    def validate_login(username, password):
        if username == "Spange Bob" and password == "1111":
            return True
        else:
            return False

class SpangeBob(Customer):
    def __init__(self, first_and_last_name, date_of_birth, address, phone_number, username, password):
        super().__init__(first_and_last_name, date_of_birth, address, phone_number, username, password)
        self.balance = 1000  # his balance
    
    def transfer_money(self, amount, recipient): 
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            print(f"Transferred {amount} euros to {recipient.name}.")
        else:
            print("Insufficient funds.")
    
    def view_balance(self):
        print(f"Current balance: {self.balance} euros.")
    
    def take_loan(self, loan_amount):
        self.balance += loan_amount
        print(f"Loan of {loan_amount} euros taken for house purchase.")

spange_bob_info = {
    "first_and_last_name": "Spange Bob",
    "username": "Spange Bob",
    "password": "1111",
    "date_of_birth": "01.01.2000",
    "address": "Bikini Bottom",
    "phone_number": "1234"
}

spange_bob = SpangeBob(**spange_bob_info)

def spange_bob_menu():
    while True:
        print("\nWhat would you like to do, Spange Bob?")
        print("1. Transfer money to Patrik.")
        print("2. View balance.")
        print("3. Take a loan to buy a house.")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter the amount to transfer: "))
            patrik_info = {
                "first_and_last_name": "Patrik",
                "username": "Patrik",
                "password": "1111",
                "date_of_birth": "01.01.2000",
                "address": "Bikini Bottom",
                "phone_number": "5678"
            }
            patrik = Customer(**patrik_info)
            spange_bob.transfer_money(amount, patrik)
        elif choice == "2":
            spange_bob.view_balance()
        elif choice == "3":
            loan_amount = float(input("Enter the loan amount: "))
            spange_bob.take_loan(loan_amount)
        elif choice == "4":
            print("Goodbye, Spange Bob!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")







