#_____________________________________________________________
# Assignment 2
#____________________________________________________________
'''
1. Define a Book class with attributes like title, author, and no_of_pages (all strings). 
Implement constructor(s) to initialize these attributes when creating a new Book object. 
Add a method called describe_book() that prints a summary of the book's information.
'''

class BOOK:
    def  __init__(self, title, author, pages, price):
        self.__title = title
        self.__author = author
        self._no_of_pages = pages
        self.price = price
    
    def describe_book(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Number of Pages: {self._no_of_pages}")
        print(f"Price: ${self.price}")

b1 = BOOK("hi", "helo", 420, 1200)
b1.describe_book()

'''
Title: hi
Author: helo
Number of Pages: 420
Price: $1200
'''