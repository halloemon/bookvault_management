from menu import print_main_menu, print_closing_menu
from message import closing_msg
from heading import print_title

books = []

while True:

    print_main_menu()

    user_input = int(input("Enter your choice: "))

    if(user_input == 0):
        closing_msg()
        break

    if(user_input == 1):
        print_title("Create a Book")

        book_name = input("Enter Book Name: ")
        book_qty = int(input("Enter Initial Book Quantity: "))

        new_book = {
            "name": book_name,
            "qty": book_qty
        }

        books.append(new_book)

        print(f"Book Name: {book_name} Successfully Added")
        print_closing_menu()
        
        user_input_add = int(input("Enter your choice: "))
        if(user_input_add == 0): 
            closing_msg()
            break
    
    if(user_input == 2):
        print_title("List of book")

        # print(books)
        print(f"{'-'*45}")
        print(f"|{"Book Name":^20} | {"Quantity":^20}|")
        print(f"{'-'*45}")

        for book in books:
            print(f"|{book['name']:^20} | {book['qty']:^20}|")
            print(f"{'-'*45}")

        print_closing_menu()
    
        user_input_add = int(input("Enter your choice: "))
        if(user_input_add == 0): 
            closing_msg()
            break
    
    if(user_input == 3):
        found = False
        print_title("Sell a Book")

        search_book_name = input("Enter Book Name: ")

        for book in books:
            inventory_book_name = book["name"]
            if(search_book_name == inventory_book_name):
                found = True
                print("The requested book Found!")
                
                sell_qty = int(input("Enter Sell Quantity: "))
                inventory_qty = book["qty"]

                if(sell_qty <= inventory_qty):
                    book["qty"] = inventory_qty - sell_qty
                
                break
        if(found == False):
           print("The requested book was not found")

        
        print_closing_menu()
    
        user_input_sell = int(input("Enter your choice: "))
        if(user_input_sell == 0): 
            closing_msg()
            break

    if(user_input == 4):
        found = False
        print_title("Update a Book")
            
        search_book_name = input("Enter Book Name: ")

        for book in books:
            inventory_book_name = book["name"]
            if(search_book_name == inventory_book_name):
                found = True
                print("The requested book Found!")
                
                update_qty = int(input("Enter Update Quantity: "))
                inventory_qty = book["qty"]

                if(update_qty > 0):
                    book["qty"] = inventory_qty + update_qty
                
                break
        if(found == False):
           print("The requested book was not found")

        
        print_closing_menu()
    
        user_input_update = int(input("Enter your choice: "))
        if(user_input_update == 0): 
            closing_msg()
            break