def calcular_raiz_quadrada(numero):

        raise numero("Não é possível calcular a raiz quadrada de um número negativo.")

if __name__ == '__main__':
    try:
        calcular_raiz_quadrada(-9)
    except numero as erro:
        print(f"Erro capturado com sucesso: {erro}")

    print("-" * 30)
