from neo4j import GraphDatabase
from player import *
from match import *

class Application:
    def __init__(self, uri, auth):
        try:
            self.driver = GraphDatabase.driver(uri, auth=auth)
        except:
            print("CONNECTION ERROR")
            
    def run(self):
        try:
            self.session = self.driver.session()
        except:
            print("ERROR ON STARTING SESSION")
            
    def close(self):
        try:
           self.session.close()
        except:
            print("ERROR ON CLOSING SESSION")
            
        try:
            self.driver.close()        
        except:
            print("ERROR ON CLOSING CONNECTION")
            
    def create_player(self, player: Player):
        try:
            self.session.run("CREATE (p:Player {name: $name})", name = player.name)
        except:
            print("ERROR ON CREATING PLAYER")

    def update_player(self, player: Player):
        try:
            self.session.run("MATCH (p:Player) WHERE ID(p) = $id SET p.name = $name", id = player.id, name = player.name)
        except:
            print("ERROR ON UPDATING PLAYER")

    def read_player(self, player):
        """ Uses player's name to find it """
        try:
            result = self.session.run("MATCH(p:Player{name: $name}) RETURN p.name AS name, ID(p) as id", name = player.name)
            record = result.single()
            name, id_ = record["name"], record["id"]
            p = Player(id_, name)
            return p           
        except:
            print("ERROR ON READING PLAYER")
   
    def delete_player(self, player):
        try:
            self.session.run("MATCH (p:Player{name: $name}) DETACH DELETE p", name = player.name)
        except:
            print("ERROR ON DELETING PLAYER")

    def create_match(self, match):
        try:
            self.session.run("CREATE (m:Match {players: $players, result: $result})", players = match.player_list, result = match.result)
        except:
            print("ERROR ON CREATING MATCH")

    def update_match(self, match):
        try:
            self.session.run("MATCH (m:Match) WHERE ID(m) = $id_ SET m.players = $players, m.result = $result", id_ = match.id, players = match.player_list, result = match.result)
        except:
            print("ERROR ON UPDATING MATCH")

    def read_match(self, match):
        try:
            result = self.session.run("MATCH (m:Match)  WHERE ID(m) = $id_ RETURN ID(m) as id, m.players as players, m.result as result", id_ = match.id)
            record = result.single()
            id_, player_list, res = record["id"], record["players"], record["result"]
            m = Match(id_, player_list, res)
            return m
        except:
            print("ERROR ON READING MATCH")

    def delete_match(self, match):
        try:
            self.session.run("MATCH (m:Match) WHERE ID(m) = $id_ DETACH DELETE m", id_ = match.id)
        except:
            print("ERROR ON DELETING MATCH")
            
    def get_player_list(self):
        try:
            result = self.session.run("MATCH (p:Player) RETURN p.name as name")
            
            res = []
            for record in result.values():
                res.append(record[0])
            
            return res
        except:
            print("ERROR ON GETTING PLAYER LIST")
            
    def get_player_match_history(self, player):
        """ Uses player's id to find it"""
        try:
            result = self.session.run("MATCH(m:Match) WHERE $id_ IN m.players RETURN ID(m) as id, m.players as players, m.result as result", id_ = player.id)
            return result.values()
        except:
            print("ERROR ON FOUNDING PLAYER'S MATCH HISTORY")
        