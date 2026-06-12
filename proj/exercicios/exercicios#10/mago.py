class mago(heroi):
    
    def __init__(self, nome, vida, poder_magico):
        # super().__init__ herda o nome e a vida da classe mãe
        super().__init__(nome, vida)
        self.poder_magico = poder_magico

    # Sobrescrevendo o método atacar
    def atacar(self):
        dano = self.poder_magico + 10
        return f"O Mago {self.nome} lançou um feitiço! Dano causado: {dano}."