from database import Database
from pymongo import MongoClient
from bson.objectid import ObjectId
from uml import *

class MotoristaDAO:
    def __init__(self):
        self.db = Database(database="atlas-cluster", collection="Motoristas")

    def create_driver(self, motorista: Motorista):
        try:
            crr = []
            for corrida in motorista.corridas:
                crr.append({"nota": corrida.nota, "distancia": corrida.distancia, "valor": corrida.valor,
                            "passageiro": {"nome": corrida.passageiro.nome, "documento": corrida.passageiro.documento}})
            
            res = self.db.collection.insert_one({"nota": motorista.nota, "corridas": crr})
            print(f"Driver created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating driver: {e}")
            return None

    def read_driver_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Driver found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading driver: {e}")
            return None

    def update_driver(self, id: str, nota: int, corrida: Corrida):
        try:
            res = self.read_driver_by_id(id)
            
            crr = res['corridas']
            crr.append({"nota": corrida[0], "distancia": corrida[1], "valor": corrida[2], "passageiro": {"nome": corrida[3], "documento": corrida[4]}})
            
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nota": nota, "corridas": crr}})
            print(f"Driver updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating driver: {e}")
            return None

    def delete_driver(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Driver deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting driver: {e}")
            return None