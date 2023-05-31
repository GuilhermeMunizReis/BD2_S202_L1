from teacher_crud import *
from teacher_cli import *
from neo4j import basic_auth

uri = "bolt://3.80.159.105:7687"
auth = basic_auth("neo4j", "depth-rocks-warranty")
teacherCRUD = Teacher_CRUD(uri, auth)
teacherCLI = TeacherCLI(teacherCRUD)

teacherCLI.run()
