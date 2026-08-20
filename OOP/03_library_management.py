"""
3. Library Management
"""

class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author
        self.is_available=True

    def borrow(self):
        if self.is_available==True:
            print("Book is available")
            x=int(input("Do u want to borrow this book, enter 1 Or 2 below-->\n1.Yes\n2.No\n"))
            if x==1:
                self.is_available=False
                print(f"The {self.name} has been borrowed")
            elif x==2:
                print("Then why u came here, Get the f_ck outta here bitch")
            else:
                print("Invalid Input")
        else:
            print("Unavailable")

    def returned(self):
        if self.is_available==False:
            n=int(input("Do you want to return the book, enter 1 Or 2 below-->\n1.Yes\n2.No\n"))
            if n==1:
                self.is_available=True
                print("Your book has been returned,Thankyou")
            elif n==2:
                print("Thankyou")
            else:
                print("Invalid option entered")
        else:
            print("Book is available in library")

    def display(self):
        print(f"{self.name}:{self.author}")

nm=input("Enter the Book's name: ")
athr=input("Enter the Author's name: ")

bk=Book(nm,athr)
bk.display()
bk.borrow()
bk.borrow()
bk.returned()
