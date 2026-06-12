from Instrumentos import Instrumentos

if __name__ == '__main__':

       instrumentos = [Violao(), Flauta(), Bateria()]
    for instrumento in instrumentos:
        print(instrumento.tocar())