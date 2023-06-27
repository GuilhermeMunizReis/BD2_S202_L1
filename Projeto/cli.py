from classes import *

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")
                
class ClansCLI(SimpleCLI):
    def __init__(self, clansCRUD):
        super().__init__()
        self.clansCRUD = clansCRUD
        self.clansCRUD.run()
        self.add_command("create_clan", self.create_clan)
        self.add_command("read_clan", self.read_clan)
        self.add_command("update_clan", self.update_clan)
        self.add_command("delete_clan", self.delete_clan)
        self.add_command("create_person", self.create_person)
        self.add_command("read_person", self.read_person)
        self.add_command("update_person", self.update_person)
        self.add_command("delete_person", self.delete_person)
        
    def create_clan(self):
        name = input("Insira o nome do clan: ")
        clan = Clan(name, [])
        
        self.clansCRUD.create_clan(clan)
    
    def read_clan(self):
        name = input("Inisra o nome clan: ")
        
        clan = Clan(name, [])
        
        res = self.clansCRUD.read_clan(clan)
        print(res)
        
        return res

    def update_clan(self):
        name = input("Inisra o nome atual do clan: ")
        newName = input("Insira o novo nome do clan: ")
        
        clan = Clan(name, [])
        
        self.clansCRUD.update_clan(clan, newName)
        
    def delete_clan(self):
        name = input("Inisra o nome do clan: ")
        
        clan = Clan(name, [])
        
        self.clansCRUD.delete_clan(clan)
    
    def create_person(self):
        name = input("Insira o nome da pessoa: ")
        age = int(input("Insira a idade da pessoa: "))
        title = input("Insira o titulo da pessoa: ")
        
        member = Member(name, age, title)
        
        clanName = input("Insira o nome do clan: ")
        
        self.clansCRUD.create_person(member, clanName)
    
    def read_person(self):
        name = input("Inisra o nome da pessoa: ")
        
        member = Member(name, None, None)
        
        res = self.clansCRUD.read_person(member)
        print(res)
        
        return res
    
    def update_person(self):
        name = input("Inisra o nome da pessoa: ")
        newAge = input("Insira a nova idade: ")
        newTitle = input("Insira o novo titulo: ")
        
        member = Member(name, None, None)
        
        self.clansCRUD.update_person(member, newAge, newTitle)
        
    def delete_person(self):
        name = input("Inisra o nome: ")
        
        member = Member(name, None, None)
        
        self.clansCRUD.delete_person(member)