import numpy as np

#Proyecto SmartHorseIA
#Elaborado por:
#Mauricio Carrillo - 2024092
#Juan Esteban Mazuera - 2043008
#Sheilly Ortega - 2040051

class Horse:

    def __init__(self,posXIA,posYIA, posXJUG, posYJUG, puntosJUG, puntosIA, mapaActual, padre, hijo, profundidad,tipo,MINMAX):
        self.posicionXIA = posXIA
        self.posicionYIA = posYIA
        self.posicionXJugador = posXJUG
        self.posicionYJugador = posYJUG
        self.puntosIA = puntosIA
        self.puntosJUG = puntosJUG
        self.mapa = mapaActual
        self.padre = padre
        self.hijo = hijo
        self.heuristicaIA = 0
        self.heuristicaJUG = 0
        self.hx = 0
        self.hy = 0
        self.profundidad = profundidad
        self.utilidad = 0
        self.tipo = tipo
        self.minimax = MINMAX
    
    #Funcion de movimiento del caballo

    def movimiento1(self):
        if(self.tipo == "Jugador"):
            if(self.mapa[self.posicionYJugador - 1][self.posicionXJugador - 2] != 8 and self.mapa[self.posicionYJugador - 1][self.posicionXJugador - 2] != 9):
                self.puntosJUG += self.mapa[self.posicionYJugador - 1][self.posicionXJugador - 2]
                self.mapa[self.posicionYJugador][self.posicionXJugador] = 0
                self.mapa[self.posicionYJugador - 1][self.posicionXJugador - 2] = 9
                self.posicionYJugador = self.posicionYJugador-1
                self.posicionXJugador = self.posicionXJugador-2
        elif(self.tipo == "IA"):
            if(self.mapa[self.posicionYIA - 1][self.posicionXIA - 2] != 8 and self.mapa[self.posicionYIA - 1][self.posicionXIA - 2] != 9):
                self.puntosIA += self.mapa[self.posicionYIA - 1][self.posicionXIA - 2]
                self.mapa[self.posicionYIA][self.posicionXIA] = 0
                self.mapa[self.posicionYIA - 1][self.posicionXIA - 2] = 8
                self.posicionYIA = self.posicionYIA-1
                self.posicionXIA = self.posicionXIA-2


    def movimiento2(self):
        if(self.tipo == "Jugador"):
            if(self.mapa[self.posicionYJugador - 2][self.posicionXJugador - 1] != 8 and self.mapa[self.posicionYJugador - 2][self.posicionXJugador - 1] != 9):
                self.puntosJUG += self.mapa[self.posicionYJugador - 2][self.posicionXJugador - 1]
                self.mapa[self.posicionYJugador][self.posicionXJugador] = 0
                self.mapa[self.posicionYJugador - 2][self.posicionXJugador - 1] = 9
                self.posicionYJugador = self.posicionYJugador-2
                self.posicionXJugador = self.posicionXJugador-1
                
        elif(self.tipo == "IA"):
            if(self.mapa[self.posicionYIA - 2][self.posicionXIA - 1] != 8 and self.mapa[self.posicionYIA - 2][self.posicionXIA - 1] != 9):
                self.puntosIA += self.mapa[self.posicionYIA - 2][self.posicionXIA - 1]
                self.mapa[self.posicionYIA][self.posicionXIA] = 0
                self.mapa[self.posicionYIA - 2][self.posicionXIA - 1] = 8
                self.posicionYIA = self.posicionYIA-2
                self.posicionXIA = self.posicionXIA-1
    
    def movimiento3(self):
        if(self.tipo == "Jugador"):
            if(self.mapa[self.posicionYJugador - 2][self.posicionXJugador + 1] != 8 and self.mapa[self.posicionYJugador - 2][self.posicionXJugador + 1] != 9):
                self.puntosJUG += self.mapa[self.posicionYJugador - 2][self.posicionXJugador + 1]
                self.mapa[self.posicionYJugador][self.posicionXJugador] = 0
                self.mapa[self.posicionYJugador - 2][self.posicionXJugador + 1] = 9
                self.posicionYJugador = self.posicionYJugador-2
                self.posicionXJugador = self.posicionXJugador+1
        elif(self.tipo == "IA"):
            if(self.mapa[self.posicionYIA - 2][self.posicionXIA + 1] != 8 and self.mapa[self.posicionYIA - 2][self.posicionXIA + 1] != 9):
                self.puntosIA += self.mapa[self.posicionYIA - 2][self.posicionXIA + 1]
                self.mapa[self.posicionYIA][self.posicionXIA] = 0
                self.mapa[self.posicionYIA - 2][self.posicionXIA + 1] = 8
                self.posicionYIA = self.posicionYIA-2
                self.posicionXIA = self.posicionXIA+1
    
    def movimiento4(self):
        if(self.tipo == "Jugador"):
            if(self.mapa[self.posicionYJugador - 1][self.posicionXJugador + 2] != 8 and self.mapa[self.posicionYJugador - 1][self.posicionXJugador + 2] != 9):
                self.puntosJUG += self.mapa[self.posicionYJugador - 1][self.posicionXJugador + 2]
                self.mapa[self.posicionYJugador][self.posicionXJugador] = 0
                self.mapa[self.posicionYJugador - 1][self.posicionXJugador + 2] = 9
                self.posicionYJugador = self.posicionYJugador-1
                self.posicionXJugador = self.posicionXJugador+2
        elif(self.tipo == "IA"):
            if(self.mapa[self.posicionYIA - 1][self.posicionXIA + 2] != 8 and self.mapa[self.posicionYIA - 1][self.posicionXIA + 2] != 9):
                self.puntosIA += self.mapa[self.posicionYIA - 1][self.posicionXIA + 2]
                self.mapa[self.posicionYIA][self.posicionXIA] = 0
                self.mapa[self.posicionYIA - 1][self.posicionXIA + 2] = 8
                self.posicionYIA = self.posicionYIA-1
                self.posicionXIA = self.posicionXIA+2
    
    def movimiento5(self):
        if(self.tipo == "Jugador"):
            if(self.mapa[self.posicionYJugador + 1][self.posicionXJugador + 2] != 8 and self.mapa[self.posicionYJugador + 1][self.posicionXJugador + 2] != 9):
                self.puntosJUG += self.mapa[self.posicionYJugador + 1][self.posicionXJugador + 2]
                self.mapa[self.posicionYJugador][self.posicionXJugador] = 0
                self.mapa[self.posicionYJugador + 1][self.posicionXJugador + 2] = 9
                self.posicionYJugador = self.posicionYJugador+1
                self.posicionXJugador = self.posicionXJugador+2
        elif(self.tipo == "IA"):
            if(self.mapa[self.posicionYIA + 1][self.posicionXIA + 2] != 8 and self.mapa[self.posicionYIA + 1][self.posicionXIA + 2] != 9):
                self.puntosIA += self.mapa[self.posicionYIA + 1][self.posicionXIA + 2]
                self.mapa[self.posicionYIA][self.posicionXIA] = 0
                self.mapa[self.posicionYIA + 1][self.posicionXIA + 2] = 8
                self.posicionYIA = self.posicionYIA+1
                self.posicionXIA = self.posicionXIA+2
    
    def movimiento6(self):
        if(self.tipo == "Jugador"):
            if(self.mapa[self.posicionYJugador + 2][self.posicionXJugador + 1] != 8 and self.mapa[self.posicionYJugador + 2][self.posicionXJugador + 1] != 9):
                self.puntosJUG += self.mapa[self.posicionYJugador + 2][self.posicionXJugador + 1]
                self.mapa[self.posicionYJugador][self.posicionXJugador] = 0
                self.mapa[self.posicionYJugador + 2][self.posicionXJugador + 1] = 9
                self.posicionYJugador = self.posicionYJugador+2
                self.posicionXJugador = self.posicionXJugador+1
        elif(self.tipo == "IA"):
            if(self.mapa[self.posicionYIA + 2][self.posicionXIA + 1] != 8 and self.mapa[self.posicionYIA + 2][self.posicionXIA + 1] != 9):
                self.puntosIA += self.mapa[self.posicionYIA + 2][self.posicionXIA + 1]
                self.mapa[self.posicionYIA][self.posicionXIA] = 0
                self.mapa[self.posicionYIA + 2][self.posicionXIA + 1] = 8
                self.posicionYIA = self.posicionYIA+2
                self.posicionXIA = self.posicionXIA+1

    def movimiento7(self):
        if(self.tipo == "Jugador"):
            if(self.mapa[self.posicionYJugador + 2][self.posicionXJugador - 1] != 8 and self.mapa[self.posicionYJugador + 2][self.posicionXJugador - 1] != 9):
                self.puntosJUG += self.mapa[self.posicionYJugador + 2][self.posicionXJugador - 1]
                self.mapa[self.posicionYJugador][self.posicionXJugador] = 0
                self.mapa[self.posicionYJugador + 2][self.posicionXJugador - 1] = 9
                self.posicionYJugador = self.posicionYJugador+2
                self.posicionXJugador = self.posicionXJugador-1
        elif(self.tipo == "IA"):
            if(self.mapa[self.posicionYIA + 2][self.posicionXIA - 1] != 8 and self.mapa[self.posicionYIA + 2][self.posicionXIA - 1] != 9):
                self.puntosIA += self.mapa[self.posicionYIA + 2][self.posicionXIA - 1]
                self.mapa[self.posicionYIA][self.posicionXIA] = 0
                self.mapa[self.posicionYIA + 2][self.posicionXIA - 1] = 8
                self.posicionYIA = self.posicionYIA+2
                self.posicionXIA = self.posicionXIA-1
    
    def movimiento8(self):
        if(self.tipo == "Jugador"):
            if(self.mapa[self.posicionYJugador + 1][self.posicionXJugador - 2] != 8 and self.mapa[self.posicionYJugador + 1][self.posicionXJugador - 2] != 9):
                self.puntosJUG += self.mapa[self.posicionYJugador + 1][self.posicionXJugador - 2]
                self.mapa[self.posicionYJugador][self.posicionXJugador] = 0
                self.mapa[self.posicionYJugador + 1][self.posicionXJugador - 2] = 9
                self.posicionYJugador = self.posicionYJugador+1
                self.posicionXJugador = self.posicionXJugador-2
        elif(self.tipo == "IA"):
            if(self.mapa[self.posicionYIA + 1][self.posicionXIA - 2] != 8 and self.mapa[self.posicionYIA + 1][self.posicionXIA - 2] != 9):
                self.puntosIA += self.mapa[self.posicionYIA + 1][self.posicionXIA - 2]
                self.mapa[self.posicionYIA][self.posicionXIA] = 0
                self.mapa[self.posicionYIA + 1][self.posicionXIA - 2]= 8
                self.posicionYIA = self.posicionYIA+1
                self.posicionXIA = self.posicionXIA-2

    #Funciones Get

    def getPosXJUG(self):
        return self.posicionXJugador
    
    def getPosYJUG(self):
        return self.posicionYJugador
    
    def getPosXIA(self):
        return self.posicionXIA
    
    def getPosYIA(self):
        return self.posicionYIA
    
    def getPuntosIA(self):
        return self.puntosIA
    
    def getPuntosJUG(self):
        return self.puntosJUG
    
    def getProfundidad(self):
        return self.profundidad
    
    def getPadre(self):
        return self.padre
    
    def getHeuristica(self):
        return self.heuristica
    
    def getMapa(self):
        return self.mapa
    
    def getTipo(self):
        return self.tipo
    
    def getMinMax(self):
        return self.minimax
    
    def getUtilidad(self):
        return self.utilidad
    
    #Funciones Set
    
    def setPuntosIA(self, cantidad):
        self.puntosIA += cantidad
    
    def setPuntosJUG(self, cantidad):
        self.puntosJUG += cantidad

    def setHeuristica(self):
        punto7X, punto7Y = -1, -1
        punto6X, punto6Y = -1, -1
        punto5X, punto5Y = -1, -1
        punto4X, punto4Y = -1, -1
        punto3X, punto3Y = -1, -1
        punto2X, punto2Y = -1, -1
        punto1X, punto1Y = -1, -1

        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                if self.mapa[i][j] == 1:
                    punto1Y = i
                    punto1X = j
                if self.mapa[i][j] == 2:
                    punto2Y = i
                    punto2X = j
                if self.mapa[i][j] == 3:
                    punto3Y = i
                    punto3X = j
                if self.mapa[i][j] == 4:
                    punto4Y = i
                    punto4X = j
                if self.mapa[i][j] == 5:
                    punto5Y = i
                    punto5X = j
                if self.mapa[i][j] == 6:
                    punto6Y = i
                    punto6X = j
                if self.mapa[i][j] == 7:
                    punto7Y = i
                    punto7X = j

        if(punto7X != -1 and punto7Y != -1):
            hx = punto7X 
            hy = punto7Y
        elif(punto6X != -1 and punto6Y != -1):
            hx = punto6X 
            hy = punto6Y
        elif(punto5X != -1 and punto5Y != -1):
            hx = punto5X 
            hy = punto5Y
        elif(punto4X != -1 and punto4Y != -1):
            hx = punto4X 
            hy = punto4Y
        elif(punto3X != -1 and punto3Y != -1):
            hx = punto3X 
            hy = punto3Y
        elif(punto2X != -1 and punto2Y != -1):
            hx = punto2X 
            hy = punto2Y
        elif(punto1X != -1 and punto1Y != -1):
            hx = punto1X 
            hy = punto1Y

        self.heuristicaIA = np.sqrt((self.hx - self.posicionXIA)**2 + (self.hy - self.posicionYIA) ** 2)
        self.heuristicaJUG = np.sqrt((self.hx - self.posicionXJugador)**2 + (self.hy - self.posicionYJugador) ** 2)

    def setUtilidad (self):
        if self.utilidad != 0: 
            self.utilidad = (self.puntosIA + self.heuristicaIA/2) - self.puntosJUG 

    def setUtilidadManual(self, cantidad, hijo):
        self.utilidad = cantidad
        self.hijo = hijo


    def setProfundidad(self):
        self.profundidad = 0
    
    def setTipo(self, tipo, minimax):
        self.tipo = tipo
        self.minimax = minimax
    
    def setInicio(self):
        self.tipo = "IA"
        self.minimax = "MAX"


   



        
