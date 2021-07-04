from typing import ClassVar


class Library:
    def __init__(self , listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("List of Books present in the library are: ")
        for book in self.books:
            print(" * " +book)

    def borrowBooks(self , bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname} . Please keep it safe. And return on given time.")
            self.books.remove(bookname)
        else:
            print(f'Sorry {bookname} is currently not available in the library. Kindly choose another book')

    def returnBook(self , bookname):
        self.books.append(bookname)
        print(f"Thanks for returning the {bookname} book . Hope you enjoyed it. Have a nice day.")

    

        



class Student:
    def requestBook(self):
        self.book = input("Enter the book name you wanted to borrow.")
        return self.book

    def returnBook(self):
        self.book = input("Enter the book name you wanted to return.")
        return self.book

if __name__ == "__main__":
    centralLibrary  = Library(["Algorithms" , "Django" , "Clrs" , "Python Notes"])
    student = Student()
    while (True):
        welcomeMsg = ''' ********Welcome to Central Library*******
        please choose an option given below :
        Press 1 to Listing all the Books.
        Press 2 to Request a Book.
        Press 3 to Return a Book.
        Press 4 to Exit a Book.
        '''
        print(welcomeMsg)

        a = int(input("Enter your choice : "))

        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBooks(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for using Central Library . Wish you have a great day ahead. ")
            exit()