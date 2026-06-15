class Heroi:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self):
        return f"{self.nome} não pode atacar porque não tem uma arma equipada!"