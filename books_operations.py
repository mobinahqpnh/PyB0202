
from os import system
clear = lambda : system("cls")


from pickle import load  
with open("books.info","rb") as books_info: 
     books = load(books_info)


def add_book():
    clear()
    global books                      #global list of all books (optional code)
    book={}
    book["title"] = input("enter title of the book : ")
    book["author"] = input("enter auther of the book : ")
    book["pages"] = int(input("enter pages of the book : "))
    book["price"] = float(input("enter price of the book : "))
    book["isbn"] = input("enter isbn of the book : ")
    books.append(book)
    input("press any key ...")

def list_books():
    clear()
    for book in books :
        print(f"Title : {book['title']}")
        print(f"Author : {book['author']}")
        print(f"Pages : {book['pages']}")
        print(f"Price : {book['price']}")
        print(f"Isbn : {book['isbn']}")
        print("------------------------------------")
    input("press any key ...")
#    print(books.__sizeof__())

def find_book():
    clear()
    isbn = input("enter ISBN to find ypur book : ")
    for book in books :
        if book["isbn"] == isbn :       
            print("-------------------------------------")
            print(f"Title : {book['title']}")
            print(f"Author : {book['author']}")
            print(f"Pages : {book['pages']}")
            print(f"Price : {book['price']}")
            print(f"ISBN : {book['isbn']}")
            print("------------------------------------")
            input("press any key ...")
            break
    else : 
        input("this book is NOT books database ")


def delete_book():
    clear()
    isbn = input("enter ISBN to delete book :")
    for book in books :
        if book["isbn"] == isbn :
            books.remove(book)
            input("book has been deleted successfully")
            break
    else :
        input("this book is NOT books database ")

def save_books():
    clear()
    from pickle import dump
    with open("books.info","wb") as books_info:
        dump(books,books_info)
        input("books has been saved successfully ")






