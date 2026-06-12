from Mago import Mago 

if __name__ == "__main__":
    # 1. Criando um herói genérico (sem classe definida)
    aprendiz = Heroi("Zezinho", 50)
    print(aprendiz.atacar())

    print("-" * 50)  # Linha separadora

    # 2. Criando um Mago (Poder Mágico = 25)
    # O dano deve ser: 25 + 10 = 35
    mago_merlin = Mago("Merlin", 80, 25)
    print(f"Herói: {mago_merlin.nome} | Vida: {mago_merlin.vida}")
    print(mago_merlin.atacar())

    print("-" * 50)

    # 3. Criando um Guerreiro (Força Física = 18)
    # O dano deve ser: 18 * 2 = 36
    guerreiro_arthur = Guerreiro("Arthur", 120, 18)
    print(f"Herói: {guerreiro_arthur.nome} | Vida: {guerreiro_arthur.vida}")
    print(guerreiro_arthur.atacar())