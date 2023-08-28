# v 3.2.0

import books_operations as bo

#---------------------------main---------------------------
while True:
    bo.clear()
    print("==================================")
    print("press A to add a book")
    print("press L to list all book")
    print("press F to find a book")
    print("press D to delete a book")
    print("press S to save a book")
    print("press Q to quit application")
    print("==================================")
    choice = input("Enter your choice : ").upper()
    if   choice == 'A' :
        bo.add_book()
    elif choice == 'L' :
        bo.list_books()
    elif choice == 'F' :
        bo.find_book()
    elif choice == 'D' :
        bo.delete_book()
    elif choice == 'S' :
        bo.save_books()
    elif choice == 'Q' :
        break
    else : input("\n\nWrong choice . press any key ..")
