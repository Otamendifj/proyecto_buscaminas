from abc import ABC, abstractmethod

class Casilla(ABC):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.revelada = False
        self.marca = None

    def revelar(self):
        if not self.revelada:
            self.revelada = True
            return self.es_mina()
        return False
    
    def marcar(self, marca):
        if not self.revelada and marca in ['bandera', 'interrogante', None]:
            self.marca = marca
            return True
        return False

    def puede_revelar(self):
        return not self.revelada and self.marca != 'bandera'

    def es_bandera(self):
        return self.marca == 'bandera'

class CasillaVacia(Casilla):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)
        self.minas_colindantes = 0

    def mostrar(self):
        return str(self.minas_colindantes) if self.minas_colindantes > 0 else " "

    def es_mina(self):
        return False

class CasillaMina(Casilla):
    def mostrar(self):
        return "*"

    def es_mina(self):
        return True
