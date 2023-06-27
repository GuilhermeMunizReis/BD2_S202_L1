from database import *
from classes import *

class Clans_CRUD(Database):       
    def __init__(self, uri, auth):
        super().__init__(uri, auth)
        
    def create_clan(self, clan): # cria um clan
        try:
            self.session.run("CREATE (c:Clan{name:$name})", name=clan.name)
        except:
            print("ERROR ON CREATING A CLAN")
            
    def read_clan(self, clan): # retorna os nomes de todos os seus membros
        try:
            result = self.session.run("MATCH(p:Person)-[:MEMBER_OF]->(c:Clan{name:$name}) RETURN c.name as clanName, p.name as memberName LIMIT 100", name=clan.name)
            res = []
            
            for record in result.values():
                res.append(record[1])
                 
            return res
        except:
            print("ERROR ON READING A CLAN")
        
    def delete_clan(self, clan): # deleta um clan e seus membros com base no name
        try:
            self.session.run("MATCH (p:Person)-[:MEMBER_OF]->(c:Clan{name:$name}) DETACH DELETE c, p", name=clan.name)
        except:
            print("ERROR ON DELETING A CLAN")

    def update_clan(self, clan, newName): # atualiza o nome de um clan
        try:
            self.session.run("MATCH (c:Clan{name:$name}) SET c.name = $newName", name=clan.name, newName = newName)
        except:
            print("ERROR ON UPDATING A CLAN")

    def create_person(self, person, clan): # cria um membro de um clan
        try:
            self.session.run("CREATE (p:Person:Member{name:$name, age:$age, title:$title})", name=person.name, age=person.age, title=person.title)
            self.session.run("MATCH (p:Person{name:$pName}), (c:Clan{name:$cName}) CREATE (p)-[:MEMBER_OF]->(c)", pName = person.name, cName = clan)
        except:
            print("ERROR ON CREATING A PERSON")
            
    def read_person(self, person): # retorna apenas uma pessoa
        try:
            result = self.session.run("MATCH (p:Person{name:$name}) RETURN p.name AS name, p.age AS age, p.title AS title LIMIT 1", name=person.name)
            res = result.single()
            
            return [res["name"], res["age"], res["title"]]
        except:
            print("ERROR ON READING A PERSON")
        
    def delete_person(self, person): # deleta uma pessoa com base no name
        try:
            self.session.run("MATCH (p:Person{name:$name}) DETACH DELETE p", name=person.name)
        except:
            print("ERROR ON DELETING A PERSON")

    def update_person(self, person, newAge, newTitle): # atualiza a idade e titulo de uma pessoa
        attr = self.read_person(person)
        
        person.age, person.title = attr[1], attr[2]
        
        if newAge == "":
            newAge = person.age
        if newTitle == "":
            newTitle = person.title
            
        try:
            self.session.run("MATCH (p:Person{name:$name}) SET p.age = $newAge, p.title = $newTitle", name=person.name, newAge=newAge, newTitle = newTitle)
        except:
            print("ERROR ON UPDATING A PERSON")