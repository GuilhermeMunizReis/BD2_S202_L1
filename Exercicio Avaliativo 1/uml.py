class Motorista:
    def __init__(self, nota, corridas):
        self.nota = nota
        self.corridas = []
        for corrida in corridas:
            self.corridas.append(Corrida(corrida.nota, corrida.distancia, corrida.valor,
                                         corrida.passageiro.nome, corrida.passageiro.documento))

class Corrida:
    def __init__(self, nota: int, distancia: float, valor: float, nome: str, documento: str):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = Passageiro(nome, documento)

class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

