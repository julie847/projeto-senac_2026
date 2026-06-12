def dividir_numeros(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'Erro: Não é possível dividir por zero'
    
if __name__ == '__main__':
    print(dividir_numeros(1, 0))