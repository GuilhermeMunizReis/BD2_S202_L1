class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        print(f"O professor {self.nome} está ministrando uma aula sobre {self.assunto}.")

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        print("O aluno NOME está presente.")

class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, aluno):

        self.alunos.append(aluno)
        

    def listar_presenca(self):
        print(f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:")

        for aluno in self.alunos:
            print(f"O aluno {aluno.nome} está presente")

professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.listar_presenca()

# Presença na aula sobre Programação Orientada a Objetos, ministrada pelo professor Lucas:
# O aluno Maria está presente.
# O aluno Pedro está presente.

