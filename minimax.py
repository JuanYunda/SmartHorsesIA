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
    inicio = time.time()
    nodo = nodoHorse
    nodo.setInicio()
    nodo.setHeuristica()
    nodo.setProfundidad()
    colaDeNodos = deque()
    colaMinimax = deque()
    colaDeNodos.append(nodo)
    colaMinimax.append(nodo)
    columnas = len(mapa[0])
    filas = len(mapa)
    #Obtengo todos los nodos posibles
    while (True):
        profundidad = nodo.getProfundidad()

        if profundidad >= profundidadMaxima:
            break

        if nodo.getMinMax() == "MAX":
            #1
            if(nodo.getPosXIA() - 2 >= 0 and nodo.getPosYIA() - 1 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(), nodo.getPuntosJUG(), nodo.getPuntosIA(), copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento1()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []

            if(nodo.getPosXIA() - 1 >= 0 and nodo.getPosYIA() - 2 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(), nodo.getPuntosJUG(), nodo.getPuntosIA(), copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento2()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []

            if(nodo.getPosXIA() + 1 < columnas and nodo.getPosYIA() - 2 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(), nodo.getPuntosJUG(), nodo.getPuntosIA(), copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento3()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []

            if(nodo.getPosXIA() + 2 < columnas and nodo.getPosYIA() - 1 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(), nodo.getPuntosJUG(), nodo.getPuntosIA(), copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento4()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []

            if(nodo.getPosXIA() + 2 < columnas and nodo.getPosYIA() + 1 < filas):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(), nodo.getPuntosJUG(), nodo.getPuntosIA(), copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento5()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []

            if(nodo.getPosXIA() + 1 < columnas and nodo.getPosYIA() + 2 < filas):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(), nodo.getPuntosJUG(), nodo.getPuntosIA(), copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento6()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []
            
            if(nodo.getPosXIA() - 1 >= 0 and nodo.getPosYIA() + 2 < filas):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(), nodo.getPuntosJUG(), nodo.getPuntosIA(), copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento7()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []
            
            if(nodo.getPosXIA() - 2 >= 0 and nodo.getPosYIA() + 1 < filas):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(), nodo.getPuntosJUG(), nodo.getPuntosIA(), copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento8()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []
            
        if nodo.getMinMax() == "MIN":

            if(nodo.getPosXJUG() - 2 >= 0 and nodo.getPosYJUG() - 1 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento1()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []

            if(nodo.getPosXJUG() - 1 >= 0 and nodo.getPosYJUG() - 2 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento2()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []

            if(nodo.getPosXJUG() + 1 < columnas and nodo.getPosYJUG() - 2 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento3()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []

            if(nodo.getPosXJUG() + 2 < columnas and nodo.getPosYJUG() - 1 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento4()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []

            if(nodo.getPosXJUG() + 2 < columnas and nodo.getPosYJUG() + 1 < filas):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento5()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []

            if(nodo.getPosXJUG() + 1 < columnas and nodo.getPosYJUG() + 2 < filas):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento6()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []
            
            if(nodo.getPosXJUG() - 1 >= 0 and nodo.getPosYJUG() + 2 < filas):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento7()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []
            
            if(nodo.getPosXJUG() - 2 >= 0 and nodo.getPosYJUG() + 1 < filas):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento8()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
                copiaMapa = []
        
        nodo = colaDeNodos.popleft()

    colaDeNodos = sorted(colaMinimax, key = Horse.getProfundidad)
    colaMinimaxCopia = deque(colaDeNodos)
    profundidad = nodo.getProfundidad()
    nodo = colaMinimaxCopia.pop()

    #Aplico Minimax para asignar utilidad a todos los nodos
    while (True):
        nodoPadre = nodo.getPadre()
        resultado = nodo
        profundidad = nodo.getProfundidad()
        if profundidad == 0:
            break 

        if profundidad == profundidadMaxima or nodo.getHijo() == None:
            nodo.setHeuristica()
            nodo.setUtilidad()
        
        if nodoPadre.getMinMax() == "MAX":
            if nodoPadre.getUtilidad() == 0 or nodoPadre.getHijo() == None:
                nodoPadre.setHeuristica()
                nodoPadre.setUtilidadManual(nodo.getUtilidad(), nodo)
            elif nodo.getUtilidad() > nodoPadre.getUtilidad():
                nodoPadre.setHeuristica()
                nodoPadre.setUtilidadManual(nodo.getUtilidad(), nodo)

        if nodoPadre.getMinMax() == "MIN":
            if nodoPadre.getUtilidad() == 0 or nodoPadre.getHijo() == None:
                nodoPadre.setHeuristica()
                nodoPadre.setUtilidadManual(nodo.getUtilidad(), nodo)
            elif nodo.getUtilidad() < nodoPadre.getUtilidad():
                nodoPadre.setHeuristica()
                nodoPadre.setUtilidadManual(nodo.getUtilidad(), nodo)
        
        if len(colaMinimaxCopia) == 0:
            break
        nodo = colaMinimaxCopia.pop()
    
    solucion = []
    utilidad = resultado.getUtilidad()
    if resultado.getHijo().getProfundidad() >= 2:
        solucion.append(resultado.getMapa())
    else:
        solucion.append(resultado.getHijo().getMapa())
    fin = time.time()
    print(resultado.getHijo().getPuntosJUG())
    return solucion, utilidad, fin-inicio, resultado.getHijo()

    

   

        


                


        
                

        




        



