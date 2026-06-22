def adicionar_nota_aluno(lista_notas, nova_nota):
    try:
        # Verifica através de condicionais se a nota está no intervalo correto
        if not (0.0 <= nova_nota <= 10.0):
            raise ValueError(f"Nota inválida ({nova_nota}). A nota deve estar entre 0.0 e 10.0.")
        
        # Se passar na validação, adiciona à lista
        lista_notas.append(nova_nota)
        print(f"Nota {nova_nota} adicionada com sucesso!")
        
    except TypeError:
        print("Erro: Tipo incorreto de dado passado para a nota.")
        
    return lista_notas

if __name__ == "__main__":
    notas_turma = [8.5, 9.0]
    
    print(" Teste 2: ValueError (Nota fora do limite) ")
    adicionar_nota_aluno(notas_turma, 12.0)
    