from database import Database
from writeAJson import writeAJson
from productAnalyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
db.resetDatabase()

# 1.Média de gasto total:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$group": {"_id": None, "media": {"$avg": "$total"}}}
])

writeAJson(result, "Média de gasto total")

# # Cliente que mais comprou em cada dia:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$sort": {"_id.data": 1, "total": -1}},
    {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
])

writeAJson(result, "Cliente que mais comprou em cada dia")

# # Produto mais vendido:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total": -1}},
    {"$limit": 1}
])
writeAJson(result, "Produto mais vendido")

# Total de vendas em cada dia 
result = ProductAnalyzer.daySales(db)

writeAJson(result, "Vendas por dia")

# Produto mais vendido em cada compra

result = ProductAnalyzer.mostSaledinEachSale(db)

writeAJson(result, "Produto mais vendido de cada compra")


# Cliente da compra mais cara

result = ProductAnalyzer.mostExpensiveSaleCustomer(db)

writeAJson(result, "Cliente da compra mais cara")

# Produtos com mais de uma unidade vendida

result = ProductAnalyzer.allProductsQuantityMoreThan1(db)

writeAJson(result, "Produtos com mais de uma unidade vendida")