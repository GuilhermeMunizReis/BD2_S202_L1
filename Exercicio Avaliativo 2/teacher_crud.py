from database import *

class Teacher_CRUD(Database):       
    def __init__(self, uri, auth):
        super().__init__(uri, auth)
        
    def create(self, name, ano_nasc, cpf): # cria um Teacher
        try:
            self.session.run("CREATE (t:Teacher{name:$name, ano_nasc:$ano_nasc, cpf:$cpf})", name=name, ano_nasc=ano_nasc, cpf=cpf)
        except:
            print("ERROR ON CREATING A TEACHER")
            
    def read(self, name): # retorna apenas um Teacher
        try:
            result = self.session.run("MATCH (t:Teacher{name:$name}) RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf LIMIT 1", name=name)
            res = result.single()
            
            return [res["name"], res["ano_nasc"], res["cpf"]]
        except:
            print("ERROR ON READING A TEACHER")
        
    def delete(self, name): # deleta Teacher com base no name
        try:
            self.session.run("MATCH (t:Teacher{name:$name} DETACH DELETE t)", name=name)
        except:
            print("ERROR ON DELETING A TEACHER")

    def update(self, name, newCpf): # atualiza cpf com base no name
        try:
            self.session.run("MATCH (t:Teacher{name:$name}) SET t.cpf = $newCpf", name=name, newCpf=newCpf)
        except:
            print("ERROR ON UPDATING A TEACHER")

    