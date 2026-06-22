class IdadeInvalidaError(Exception):
    pass

    def cadrastar_eleitor(idade):
        if idade < 16:
    raise IdadeInvalidaError("Idade mínima para cadastro de eleitor é 16 anos.")
    
    return "Eleitor cadastrado com sucesso!"

if __name__ == '__main__':
    try:
        print(cadastrar_eleitor(18))
    except IdadeInvalidaError as erro:
        print(f"Erro: {erro}")
        
    try:
        print(cadastrar_eleitor(14))
    except IdadeInvalidaError as erro:
        print(f"Erro capturado: {erro}")