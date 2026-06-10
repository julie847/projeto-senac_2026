###########################  exercicios aula 1/6  ########################### 


def calcula_area_triangulo (base: float, altura: float):
    area = (base * altura) /2
    print (F"A area do triângulo é: {area}")


    def converte_temperatura_fahrenreit(graus_celsius: float):
         celsius = (fahrenreit - 32) * 5/9
        temperatura = (graus_celsisus * (9/5)) - 32
        print (F" A temperatura em fahrenreit é {temperatura}")


        def converte_em_dolares (reais: float):
            dolares = reais / 5.04
            print (f"O valor em dólarers é: {dolares}")

 def calcula_salario_apos_desconto ( salario: float ):
     salario_resultante = salario - (salario * (15/100))
          return salario_resultante



          ############################## Exercicos aula 02/06 ############################## 


          def classificar_pop(idade: int) -> str:

         if idade <12:
            return "Criança"

         elif idade >12 and idade < 18:
             return "adolescente"

             elif idade >= 18 and idade <=60
             return "adulto"

         else:    ''
             return "idoso"

             ############################ aula 03/06 #######################

              def ultimo_animal(animais: list):
...     return animais[-1]
... 2
>>> animais = ['gato', 'cachorro', 'passarinho', 'coelho']
>>> ultimo_animal(animais)
'coelho'
>>> 

3
def adicionar_compras(compras: list):
...     compras.append("arroz")
...     compras.append("feijao")
...     compras.append("batata")
... 
...     return compras 
...     
>>>

4
 def quantidade_notas(notas: list):
...       return len(notas)
...       
>>> notas_alunos = [7.5, 8.0, 6.0, 9.5, 10.0]
>>> quantidade_notas(notas_alunos)
5

5
def mudar_cor (cores: list):
...       cores[1] = "amarelo"
...       return cores
... 
>>> lista_cores = ['vermelho',' verde', 'azul']
>>> mudar_cor(lista_cores)
['vermelho', 'amarelo', 'azul']
>>> 

7
def contar_sim(respostas):
...   return respostas.count('Sim')
respostas = ['Sim', 'Não', 'Sim', 'Sim', 'Não', 'Sim']
>>> respostas.count('Sim')
4














