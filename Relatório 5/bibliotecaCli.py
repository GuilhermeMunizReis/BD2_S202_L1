from pymongo import MongoClient
from bson.objectid import ObjectId
from cli import SimpleCLI

class BibliotecaModel:
    def __init__(self, database):
        self.db = database

    def create_book(self, title: str, author: str, year: int, price: float):
        try:
            res = self.db.collection.insert_one({"titulo": title, "autor": author, "ano": year, "preco": price})
            print(f"Book created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating book: {e}")
            return None

    def read_person_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Book found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading book: {e}")
            return None

    def update_person(self, title: str, author: str, year: int, price: float):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"titulo": title, "autor": author, "ano": year, "preco": price}})
            print(f"Book updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating book: {e}")
            return None

    def delete_person(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Book deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting book: {e}")
            return None

class BibliotecaCLI(SimpleCLI):
    def __init__(self, biblioteca_model):
        super().__init__()
        self.biblioteca_model = biblioteca_model
        self.add_command("create", self.create_book)
        self.add_command("read", self.read_book)
        self.add_command("update", self.update_book)
        self.add_command("delete", self.delete_book)
        
    def create_book(self):
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        year = int(input("Enter the year: "))
        price = float(input("Enter the price: "))
        self.biblioteca_model.create_book(title, author, year, price)

    def read_book(self):
        id = input("Enter the id: ")
        book = self.biblioteca_model.read_person_by_id(id)
        if book:
            print(f"Title: {book['titulo']}")
            print(f"Author: {book['autor']}")
            print(f"Year: {book['ano']}")
            print(f"Price: {book['preco']}")
            
    def update_book(self):
        id = input("Enter the id: ")
        title = input("Enter the new title: ")
        author = input("Enter the new author: ")
        year = int(input("Enter the new year: "))
        price = float(input("Enter the new price: "))
        self.biblioteca_model.update_person(id, title, author, year, price)

    def delete_book(self):
        id = input("Enter the id: ")
        self.biblioteca_model.delete_person(id)
        
    def run(self):
        print("Welcome to the book CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()