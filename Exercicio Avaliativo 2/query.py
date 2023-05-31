from database import *
from neo4j import basic_auth

uri = "bolt://3.80.159.105:7687"
auth = basic_auth("neo4j", "depth-rocks-warranty")
app = Database(uri, auth)

app.run()

#====================================================================
#                           QUESTÃO 1
#====================================================================
res = app.session.run("MATCH(t:Teacher{name:$nome}) RETURN t.ano_nasc as ano_nasc, t.cpf as cpf", nome="Renzo")
record = res.single()
print(record["ano_nasc"], record["cpf"])
print()

res = app.session.run("MATCH(t:Teacher) WHERE left(t.name, 1) = \"M\" RETURN t.name as name, t.cpf as cpf")
record = res.values()
for i in record:
    print(i[0], i[1])
print()

res = app.session.run("MATCH(c:City) RETURN c.name as name")
record = res.values()
for i in record:
    print(i[0])
print()

res = app.session.run("MATCH(s:School) WHERE s.number >=150 AND s.number <=550 RETURN s.name as name, s.address as address, s.number as number")
record = res.values()
for i in record:
    print(i[0], i[1], i[2])
print()

#====================================================================
#                           QUESTÃO 2
#====================================================================

res = app.session.run("MATCH(t:Teacher) RETURN min(t.ano_nasc), max(t.ano_nasc)")
record = res.single()
print(record[0], record[1])
print()

res = app.session.run("MATCH(c:City) RETURN avg(c.population)")
record = res.single()
print(round(record[0], 2))
print()

res = app.session.run("MATCH(c:City{cep: \"37540-000\"}) RETURN REPLACE(c.name, \"a\", \"A\")")
record = res.single()
print(record[0])
print()

res = app.session.run("MATCH(t:Teacher) RETURN RIGHT(t.name, size(t.name)-3)")
record = res.values()
for i in record:
    print(i[0])
print()
