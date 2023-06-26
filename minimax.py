from collections import deque
import matplotlib.pyplot as plt
import copy
from horse import Horse
import subprocess
import time

#Proyecto SmartHorseIA
#Elaborado por:
#Mauricio Carrillo - 2024092
#Juan Esteban Mazuera - 2043008
#Sheilly Ortega - 2040051

def minimax(mapa,profundidadMaxima,nodoHorse):
    profundidad = 0
    horse1X, horse1Y = 0, 0
    horse2X, horse2Y = 0, 0

    inicio = time.time()

    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 8:
                horse1Y = i
                horse1X = j
            if mapa[i][j] == 9:
                horse2Y = i
                horse2X = j

    nodo = nodoHorse
    nodo.setInicio()
    nodo.setHeuristica()
    colaDeNodos = deque()
    colaMinimax = deque()

    #Obtengo todos los nodos posibles
    while (True):
        profundidad = nodo.getProfundidad()
        if profundidad > profundidadMaxima:
            break

        if nodo.getMinMax() == "MAX":
            #1
            if(nodo.getPosXIA() - 2 >= 0 and nodo.getPosYIA() - 1 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(), nodo.getPuntosJUG(), nodo.getPuntosIA(), copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento1()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXIA() - 1 >= 0 and nodo.getPosYIA() - 2 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento2()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXIA() + 1 < len(nodo.getMapa()[0]) and nodo.getPosYIA() - 2 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento3()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXIA() + 2 < len(mapa[0]) and nodo.getPosYIA() - 1 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento4()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXIA() + 2 < len(mapa[0]) and nodo.getPosYIA() + 1 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento5()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXIA() + 1 < len(mapa[0]) and nodo.getPosYIA() + 2 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento6()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
            
            if(nodo.getPosXIA() - 1 >= 0 and nodo.getPosYIA() + 2 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento7()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
            
            if(nodo.getPosXIA() - 2 >= 0 and nodo.getPosYIA() + 1 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento8()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
            
        if nodo.getMinMax() == "MIN":

            if(nodo.getPosXJUG() - 2 >= 0 and nodo.getPosYJUG() - 1 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento1()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXJUG() - 1 >= 0 and nodo.getPosYJUG() - 2 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento2()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXJUG() + 1 < len(mapa[0]) and nodo.getPosYJUG() - 2 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento3()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXJUG() + 2 < len(mapa[0]) and nodo.getPosYJUG() - 1 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento4()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXJUG() + 2 < len(mapa[0]) and nodo.getPosYJUG() + 1 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento5()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXJUG() + 1 < len(mapa[0]) and nodo.getPosYJUG() + 2 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento6()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
            
            if(nodo.getPosXJUG() - 1 >= 0 and nodo.getPosYJUG() + 2 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento7()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
            
            if(nodo.getPosXJUG() - 2 >= 0 and nodo.getPosYJUG() + 1 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento8()
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
        
        nodo = colaDeNodos.popleft()
    
    colaOriginal = deque(colaMinimax)
    colaMinimax = sorted(colaOriginal, key=nodo.getProfundidad)
    colaMinimaxCopia = deque(colaMinimax)
    colaRecorrida = deque()
    
    nodo = colaMinimax.popleft()

    #Asigno utilidad a todos los nodos de la mayor profundidad una utilidad
    profundidad = nodo.getProfundidad()
    while (profundidad == profundidadMaxima):
        nodo.setUtilidad()
        profundidad = nodo.getProfundidad()
        nodo = colaMinimax.popleft()
    
    colaMinimax = deque(colaMinimaxCopia)

    #Aplico Minimax para asignar utilidad a todos los nodos
    while (True):
        resultado = nodo
        profundidad = nodo.getProfundidad()
        if profundidad == 0:
            colaRecorrida.append(nodo)
            resultado = nodo
            break 
        
        if nodo.getPadre().getTipo() == "MAX":
            if nodo.getPadre().getUtilidad() == 0:
                nodo.getPadre().setUtilidadManual(nodo.getUtilidad(), nodo)
            elif nodo.getUtilidad() > nodo.getPadre().getUtilidad():
                nodo.getPadre().setUtilidadManual(nodo.getUtilidad(), nodo)

        if nodo.getPadre().getTipo() == "MIN":
            if nodo.getPadre().getUtilidad() == 0:
                nodo.getPadre().setUtilidadManual(nodo.getUtilidad(), nodo)
            elif nodo.getUtilidad() < nodo.getPadre().getUtilidad():
                nodo.getPadre().setUtilidadManual(nodo.getUtilidad(), nodo)
            
        nodo = colaMinimax.popleft()
    
    solucion = []
    utilidad = resultado.getUtilidad()
    solucion.append(resultado.getHijo().getMapa())
    #while resultado.getHijo() != None:
     #   solucion.append(resultado.getMapa())
      #  resultado = resultado.getHijo()
    fin = time.time()

    #solucion.append(mapa)

    return solucion, utilidad, fin-inicio, resultado.getHijo()

    

   

        


                


        
                

        




        



