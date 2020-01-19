class Book:
    def __init__(self, name, author):
        self.name=name
        self.author=author
    def getName(self):
        return self.name
    def setName(self, name):
        self.name=name
    def getAuthor(self):
        return self.author

Books = []

def newBook():
    name = input('Name: ')
    author = input('Author: ')
    b = Book(name,author)
    Books.append(b)
def displayBook():
    for i in Books:
        print('Name',i.getName())
        print('Author',i.getAuthor())
def delBook():
    name=input('Enter book name to delete: ')
    for i in Books:
        if i.getName()==name:
            Books.remove(i)
def editBook():
    name=input('Enter book name to edit: ')
    for i in Books:
        if i.getName()==name:
            newName=input('Enter new name: ')
            i.setName(newName)
def menu():
    print('1. Add Book')
    print('2. Display Book')
    print('3. Delete Book')
    print('4. Edit Book')
    print('5. Exit')
    choice = int(input())
    return choice
while True:
    choice = menu()
    if choice == 5:
        print('Thanks\n')
        break;
    else:
        if choice == 1:
            newBook()
        elif choice == 2:
            displayBook()
        elif choice == 3:
            delBook()
        else:
            editBook()
