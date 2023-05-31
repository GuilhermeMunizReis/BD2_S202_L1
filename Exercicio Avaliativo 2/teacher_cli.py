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
                
class TeacherCLI(SimpleCLI):
    def __init__(self, teacherCRUD):
        super().__init__()
        self.teacherCRUD = teacherCRUD
        self.teacherCRUD.run()
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)
        
    def create_teacher(self):
        name = input("Insira o nome: ")
        ano_nasc = int(input("Insira o ano de nascimento: "))
        cpf = input("Insira o CPF: ")
        
        self.teacherCRUD.create(name, ano_nasc, cpf)
    
    def read_teacher(self):
        name = input("Inisra o nome: ")
        
        res = self.teacherCRUD.read(name)
        print(res)
            
    def update_teacher(self):
        name = input("Inisra o nome: ")
        cpf = input("Insira o CPF: ")
        
        self.teacherCRUD.update(name, cpf)
        
    def delete_teacher(self):
        name = input("Inisra o nome: ")
        
        self.teacherCRUD.delete(name)