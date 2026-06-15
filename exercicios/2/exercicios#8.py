class Produto:
    def __init__(self, nome, preco):
        if preco <= 0:
            raise ValueError("O preço do produto deve ser maior que zero.")
        
        self.nome = nome
        self.preco = preco

if __name__ == '__main__':
    try:
        p2 = Produto("Caneta", 0)
    except ValueError as erro:
        print(f"Erro capturado com sucesso: {erro}")