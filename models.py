import random

class Carta:
    def __init__(self, nome, atributos):
        self.nome = nome
        self.atributos = atributos

    def __str__(self):
        atributos_str = "\n".join([f"{k}: {v}" for k, v in self.atributos.items()])
        return f"{self.nome}\n{atributos_str}"

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.baralho = []

    def tem_cartas(self):
        return len(self.baralho) > 0

    def puxar_carta(self):
        return self.baralho.pop(0) if self.tem_cartas() else None

    def ganhar_cartas(self, cartas):
        self.baralho.extend(cartas)

    def embaralhar(self):
        random.shuffle(self.baralho)
