import os
import CRUD as CRUD

if __name__ == "__main__":
    operation_system = os.name

    CRUD.init_console()

while(True):
    print('\n\n============ Main Menu Purwadhika Library ============\n')

    menu_utama = input('''1. Check books availibility
2. Add new book
3. Edit books availibility
4. Delete book availibility
5. Exit\n
Silahkan pilih menu [1-5]: ''')

    if menu_utama == "1":
        print("\n"+"="*55)
        read_menu = input('''\n1. Check all books data
2. Check book data by ISBN
3. Back to main menu\n
Please select menu [1-3]: ''')
        if read_menu == '1':
            CRUD.read_all_console()
        elif read_menu == '2':
            CRUD.read_ISBN_console()
        elif read_menu == '3':
            continue

    elif menu_utama == "2":    
        CRUD.add_console()

    elif menu_utama == "3":
        CRUD.edit_console()
        
    elif menu_utama == "4":
        CRUD.delete_console()
        
    elif menu_utama == "5":
        print("\nTerima kasih\n")
        break

    