from database import Database

class ProductAnalyzer:
    @staticmethod 
    def daySales(data):
        """ Retorna o total de vendas em cada dia"""
    
        result = data.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
        ])
        
        return result
    
    @staticmethod
    def mostSaledinEachSale(data):
        result = data.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$sort": {"produtos.quantidade": -1}},
            {"$group": {"_id": {"cliente": "$cliente_id", "compra": "$data_compra"}, "produto": {"$first": {"descricao": "$produtos.descricao", "quantidade": "$produtos.quantidade"}}}}
            ])
        
        return result
    
    @staticmethod
    def mostExpensiveSaleCustomer(data):
        result = data.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "compra": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        
        return result
    
    @staticmethod
    def allProductsQuantityMoreThan1(data):
        result = data.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"total" : {"$gt": 1}}}
        ])
        
        return result
    
"""
1. Retorne o total de vendas por dia
2. Retorne o produto mais vendido em todas as compras.
3. Encontre o cliente que mais gastou em uma única compra.
4. Liste todos os produtos que tiveram uma quantidade vendida acima de 1 unidades.
"""