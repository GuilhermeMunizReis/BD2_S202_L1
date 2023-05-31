from neo4j import GraphDatabase

class Database:
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