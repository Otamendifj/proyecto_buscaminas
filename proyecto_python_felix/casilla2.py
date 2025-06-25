class Casilla:  #Se define la clase padre de los 2 tipos de casillas
    def __init__(self, mina, oculta = True, seleccionada = False,):
        self.seleccionada = seleccionada
        self.oculta = oculta
        self.mina = mina


class Sin_mina(Casilla): #Clase de casilla que no tienen mina
    def __init__(self, oculta, seleccionada):
        super().__init__(oculta = oculta, seleccionada = seleccionada, mina = False)
        self.mina = False

class Con_mina(Casilla):  #Clase de casilla que si tiene mina
    def __init__(self, oculta, seleccionada):
        super().__init__(oculta = oculta, seleccionada = seleccionada, mina = True)