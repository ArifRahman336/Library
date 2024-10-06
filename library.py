#Entities: Book, User, Library

# functionalities: adding user, adding books, borrow, return

class Book:
    def __init__(self,id,name) -> None:
        self.id = id
        self.name = name

class User:
    def __init__(self,id,name,password) -> None:
        self.id = id
        self.name = name
        self.password = password