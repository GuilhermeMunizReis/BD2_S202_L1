from cli import SimpleCLI
from uml import *

class MotoristaCLI(SimpleCLI):
    def __init__(self, motoristaDAO):
        super().__init__()
        self.motoristaDAO = motoristaDAO
        self.add_command("create", self.create_driver)
        self.add_command("read", self.read_driver)
        self.add_command("update", self.update_driver)
        self.add_command("delete", self.delete_driver)

    def create_driver(self):        
        n = int(input("Enter the quantity of runs: "))
        corridas = []
        
        for i in range(n):
            nome = input("Enter the name: ")
            documento = input("Enter the documento: ")
            passageiro = Passageiro(nome, documento)
            
            nota = int(input("Enter the review: "))
            distancia = float(input("Enter the distance: "))
            valor = float(input("Enter the cost: "))
            corrida = Corrida(nota, distancia, valor, passageiro.nome, passageiro.documento)
            
            corridas.append(corrida)
        
        nota = int(input("Enter the grade: "))
        motorista = Motorista(nota, corridas)
        self.motoristaDAO.create_driver(motorista)

    def read_driver(self):
        id = input("Enter the id: ")
        driver = self.motoristaDAO.read_driver_by_id(id)
        if driver:
            print(f"Nota: {driver['nota']}")
            print(f"Corridas: {driver['corridas']}")

    def update_driver(self):
        id = input("Enter the id: ")
        grade = input("Enter the new grade: ")
        
        nome = input("Enter the name: ")
        documento = input("Enter the documento: ")
        passageiro = Passageiro(nome, documento)
        
        nota = int(input("Enter the review: "))
        distancia = float(input("Enter the distance: "))
        valor = float(input("Enter the cost: "))
        
        corrida = Corrida(nota, distancia, valor, passageiro.nome, passageiro.documento)
    
        self.motoristaDAO.update_driver(id, grade, corrida)

    def delete_driver(self):
        id = input("Enter the id: ")
        self.motoristaDAO.delete_driver(id)
        
    def run(self):
        print("Welcome to the driver CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()