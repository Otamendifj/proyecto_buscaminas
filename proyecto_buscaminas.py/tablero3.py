from casilla3 import CasillaVacia, CasillaMina
import random

class Tablero:
    def __init__(self, filas, columnas, cantidad_minas=0):
        self.filas = filas
        self.columnas = columnas
        self.cantidad_minas = cantidad_minas
        self.casillas = []
        self.inicializar_tablero()
        self.colocar_minas()
        self.actualizar_minas_colindantes()

#ESTE MÉTODO CREA MATRICES VACÍAS PARA CADA CASILLA
    def inicializar_tablero(self):
        self.casillas = [
            [CasillaVacia(f, c) for c in range(self.columnas)]
            for f in range(self.filas)
        ]

#COLOCA LAS MINAS ALEATORIAMENTE
    def colocar_minas(self):
        if self.cantidad_minas <= 0:
            return
        #POSICIONES RANDOM
        posiciones = random.sample(
            [(f, c) for f in range(self.filas) for c in range(self.columnas)],
            self.cantidad_minas
        )
        #DE LAS CASILLAS VACÍAS ASIGNA AHORA LAS MINAS
        for f, c in posiciones:
            self.casillas[f][c] = CasillaMina(f, c)

#CONTAMOS CON UN CONTADOR LAS MINAS ALREDEDOR BASADAS EN LA POSICION 8 CASILLAS
    def contar_minas_alrededor(self, fila, columna):
        count = 0
        for f in range(max(0, fila-1), min(self.filas, fila+2)):
            for c in range(max(0, columna-1), min(self.columnas, columna+2)):
                if (f != fila or c != columna) and isinstance(self.casillas[f][c], CasillaMina):
                    count += 1
        return count
    

    def actualizar_minas_colindantes(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                if isinstance(self.casillas[f][c], CasillaVacia):
                    self.casillas[f][c].minas_colindantes = self.contar_minas_alrededor(f, c)
    
                    
    def revelar_colindantes(self, fila, columna):
        """Función auxiliar recursiva para revelar casillas adyacentes"""
        for f in range(max(0, fila-1), min(self.filas, fila+2)):
            for c in range(max(0, columna-1), min(self.columnas, columna+2)):
                # No revelar la casilla central nuevamente
                if f == fila and c == columna:
                    continue
                    
                # Si la casilla no está revelada y no es mina
                if not self.casillas[f][c].revelada and not isinstance(self.casillas[f][c], CasillaMina):
                    self.casillas[f][c].revelada = True
                    
                    # Si no tiene minas alrededor, seguir expandiendo
                    if self.casillas[f][c].minas_colindantes == 0:
                        self.revelar_colindantes(f, c)


    def revelar_casilla(self, fila, columna):
        """Revela una casilla y sus adyacentes si no hay minas alrededor (recursivo)"""
        # Si la casilla ya está revelada o tiene bandera, no hacer nada
        if self.casillas[fila][columna].revelada or self.casillas[fila][columna].es_bandera():
            return
        
        # Revelar la casilla actual
        self.casillas[fila][columna].revelada = True
        
        # Si es mina, terminar (no revelar adyacentes)
        if isinstance(self.casillas[fila][columna], CasillaMina):
            return
        
        # Si no hay minas alrededor, revelar recursivamente las adyacentes
        if self.casillas[fila][columna].minas_colindantes == 0:
            self.revelar_colindantes(fila, columna)

