#Entities: Book, User, Library

# functionalities: adding user, adding books, borrow, return

class Book:
    def __init__(self,id,name,cat,quantity) -> None:
        self.id = id
        self.name = name
        self.cat = cat
        self.quantity = quantity

class User:
    def __init__(self,id,name,password) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.borrowedBooks = []

class Library:
    def __init__(self,owner,name) -> None:
        self.owner = owner
        self.name = name
        self.books = []
        self.users = []
    
    def addBook(self,id,name,cat,quantity):
        book = Book(id,name,cat,quantity)
        self.books.append(book)

        print(f'\n\t{name} Book added')
    
    def addUser(self,id,name,password):
        user = User(id,name,password)
        self.users.append(user)
        return user

    def borrowBook(self,user,id):
        for book in self.books:
            if book.id == id:
                if book in user.borrowedBooks:
                    print('\n\tAlready Borrowed !')
                    return
                elif book.quantity<1:
                    print('\n\tN available Copies !')
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quantity -= 1
                    print(f'\n\t{book.name} borrowed successfully !')
                    return
        print(f'\n\tBook not found !')


p1 = Library('Arif Rahman','Bookie')
admin = p1.addUser(1,'admin','admin')
rahim = p1.addUser(3,'Rahim','1234')
pybook = p1.addBook(15,'Dune','Sci-Fi',5)

run = True
currentUser = admin

while run:
    if currentUser == None:
        print(f'\n\tNo logged in user !')
        
        option = input('Login ? Registration (L/R): ')

        if option == 'R':
            id = int(input('\tEnter id: '))
            name = input('\tEnter name: ')
            password = input('\tEnter password: ')

            user = p1.addUser(id,name,password)
            currentUser = user

        elif option == 'L':
            id = int(input('\tEnter id: '))
            password = input('\tEnter password: ')

            match = False
            for user in p1.users:
                if user.id == id and user.password == password:
                     currentUser = user
                     match = True
                     break
                
                if match == False:
                    print(f'\n\tNo user found !')

    else:

        if currentUser.name == 'admin':
            print('Options: \n')

            print('1 : Add Book')
            print('2 : Show Users')
            print('3 : Show Books')
            print('4 : Logout')

            ch = int(input('\nEnter Option: '))

            if ch == 1:
                id = int(input('\tEnter id: '))
                name = input('\tEnter Name: ')
                q = int(input('\tEnter quantity: '))
                cat = input('\tEnter cat: ')

                p1.addBook(id,name,cat,q)
            
            elif ch==4:
                currentUser = None
        
        else:
            print('Options: \n')

            print('1 : Borrow Book')
            print('2 : Return Book')
            print('3 : Show Books')
            print('4 : Show Borrowed Books')
            print('5 : Show Returned Books')
            print('6 : Logout')

            ch = int(input('\nEnter Optiion: '))

            if ch==1:
                p1.borrowBook(currentUser,id)
