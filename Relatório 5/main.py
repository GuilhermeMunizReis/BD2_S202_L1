from database import Database
from writeAJson import writeAJson
from bibliotecaCli import BibliotecaCLI, BibliotecaModel

db = Database(database="biblioteca", collection="livros")
bibliotecaModel = BibliotecaModel(database=db)


bibliotecaCLI = BibliotecaCLI(bibliotecaModel)
bibliotecaCLI.run()
