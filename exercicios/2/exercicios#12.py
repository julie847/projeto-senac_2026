def buscar_letra_na_lista(lista_de_strings, indice_lista, indice_palavra):
    try:
        palavra = lista_de_strings[indice_lista]
        letra = palavra[indice_palavra]
        return letra
        
    except IndexError as erro:
        print(f"Erro detectado: {str(erro)}")
        return None
    
frutas = ["Maçã", "Banana", "Uva"]

print("--- Cenário 1: Sucesso ---")

print(f"Resultado: {buscar_letra_na_lista(frutas, 1, 0)}") 

print("\n--- Cenário 2: Falha no Índice da Lista ---")
# Índice 5 não existe na lista de frutas
buscar_letra_na_lista(frutas, 5, 0)

print("\n--- Cenário 3: Falha no Índice da Palavra (String) ---")
buscar_letra_na_lista(frutas, 2, 10)