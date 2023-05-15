from crud import *
from neo4j import basic_auth

uri = "bolt://3.239.160.150:7687"
auth = basic_auth("neo4j", "comparisons-wiggles-clip")
app = Application(uri, auth)
app.run()

#p1 = Player(None, "Adalberto")
#app.create_player(p1)
#p1 = app.read_player(p1)
#p1.name = "ADALBERTO"
#app.update_player(p1)
#app.delete_player(p1)

#m1 = Match(None, [0, 1], "red")
#app.create_match(m1)
#m1.id = 5
#m1 = app.read_match(m1)
#print(m1)
#m1.player_list = [0, 1, 3]
#app.update_match(m1)
#app.delete_match(m1)

#app.get_player_list()

#p = Player(None, "Robert")
#p = app.read_player(p)
#mh = app.get_player_match_history(p)
#print(mh)

app.close()