from crud import *
from cli import *
from neo4j import basic_auth
from classes import *

uri = "bolt://44.212.55.124:7687"
auth = basic_auth("neo4j", "washing-gyroscopes-tug")
clansCRUD = Clans_CRUD(uri, auth)
clansCLI = ClansCLI(clansCRUD)

clansCLI.run()
clansCRUD.close()