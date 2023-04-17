from database import Database
from writeAJson import writeAJson
from motoristaDAO import MotoristaDAO
from motoristaCLI import MotoristaCLI

motoristaDAO = MotoristaDAO()
motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()
