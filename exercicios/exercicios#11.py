
class AnatomiaError(Exception):
    """Exceção lançada quando uma classe abstrata tenta executar uma ação indesejada."""
    pass


class Instrumento:
    def tocar(self):
        raise AnatomiaError("Classes abstratas não tocam som.")


class Guitarra(Instrumento):
    def tocar(self):
        return " A guitarra está tocando com distorção pesada."

print("")
instrumento_generico = Instrumento()
try:
    instrumento_generico.tocar()
except AnatomiaError as e:
    print(f"Erro capturado com sucesso: {e}")

