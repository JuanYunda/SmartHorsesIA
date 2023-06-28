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
    nodo.setProfundidad()
    colaDeNodos = deque()
    colaMinimax = deque()
    colaDeNodos.append(nodo)
    colaMinimax.append(nodo)

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

            if(nodo.getPosXIA() - 1 >= 0 and nodo.getPosYIA() - 2 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento2()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXIA() + 1 < len(mapa[0]) and nodo.getPosYIA() - 2 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento3()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXIA() + 2 < len(mapa[0]) and nodo.getPosYIA() - 1 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento4()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXIA() + 2 < len(mapa[0]) and nodo.getPosYIA() + 1 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento5()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXIA() + 1 < len(mapa[0]) and nodo.getPosYIA() + 2 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento6()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
            
            if(nodo.getPosXIA() - 1 >= 0 and nodo.getPosYIA() + 2 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento7()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
            
            if(nodo.getPosXIA() - 2 >= 0 and nodo.getPosYIA() + 1 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"IA","MAX")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento8()
                nuevoNodo.setTipo("Jugador", "MIN")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
            
        if nodo.getMinMax() == "MIN":

            if(nodo.getPosXJUG() - 2 >= 0 and nodo.getPosYJUG() - 1 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento1()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXJUG() - 1 >= 0 and nodo.getPosYJUG() - 2 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento2()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXJUG() + 1 < len(mapa[0]) and nodo.getPosYJUG() - 2 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento3()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXJUG() + 2 < len(mapa[0]) and nodo.getPosYJUG() - 1 >= 0):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento4()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXJUG() + 2 < len(mapa[0]) and nodo.getPosYJUG() + 1 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento5()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)

            if(nodo.getPosXJUG() + 1 < len(mapa[0]) and nodo.getPosYJUG() + 2 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento6()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
            
            if(nodo.getPosXJUG() - 1 >= 0 and nodo.getPosYJUG() + 2 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento7()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
            
            if(nodo.getPosXJUG() - 2 >= 0 and nodo.getPosYJUG() + 1 < len(mapa)):
                copiaMapa = copy.deepcopy(nodo.getMapa())
                nuevoNodo = Horse(nodo.getPosXIA(),nodo.getPosYIA(),nodo.getPosXJUG(),nodo.getPosYJUG(),nodo.getPuntosJUG(), nodo.getPuntosIA(),copiaMapa,nodo, None,nodo.getProfundidad()+1,"Jugador","MIN")
                nuevoNodo.setHeuristica()
                nuevoNodo.movimiento8()
                nuevoNodo.setTipo("IA", "MAX")
                colaDeNodos.append(nuevoNodo)
                colaMinimax.append(nuevoNodo)
        
        nodo = colaDeNodos.popleft()

    colaDeNodos = sorted(colaMinimax, key = Horse.getProfundidad)
    colaMinimaxCopia = deque(colaDeNodos)
    nodo = colaMinimaxCopia.pop()

    #Asigno utilidad a todos los nodos de la mayor profundidad una utilidad
    profundidad = nodo.getProfundidad()

    #while (True):
     #   if profundidad != profundidadMaxima:
      #      break
       # else:
        #    nodo.setHeuristica()
         #   nodo.setUtilidad()
          #  if len(colaMinimaxCopia) == 0:
           #     break
            #else: 
             #   nodo = colaMinimaxCopia.pop()
              #  profundidad = nodo.getProfundidad()
    
    #colaMinimaxCopia = deque(colaDeNodos)
    #nodo = colaMinimaxCopia.pop()

    #Aplico Minimax para asignar utilidad a todos los nodos
    while (True):
        nodoPadre = nodo.getPadre()
        resultado = nodo
        profundidad = nodo.getProfundidad()
        if profundidad == 0 or len(colaMinimaxCopia) == 0 or nodoPadre == None:
            break 

        if profundidad == profundidadMaxima:
            nodo.setHeuristica()
            nodo.setUtilidad()
        
        if nodoPadre.getMinMax() == "MAX":
            if nodoPadre.getUtilidad() == 0:
                nodoPadre.setHeuristica()
                nodoPadre.setUtilidadManual(nodo.getUtilidad(), nodo)
            elif nodo.getUtilidad() > nodoPadre.getUtilidad():
                nodoPadre.setHeuristica()
                nodoPadre.setUtilidadManual(nodo.getUtilidad(), nodo)

        if nodoPadre.getMinMax() == "MIN":
            if nodoPadre.getUtilidad() == 0:
                nodoPadre.setHeuristica()
                nodoPadre.setUtilidadManual(nodo.getUtilidad(), nodo)
            elif nodo.getUtilidad() < nodoPadre.getUtilidad():
                nodoPadre.setHeuristica()
                nodoPadre.setUtilidadManual(nodo.getUtilidad(), nodo)
            
        nodo = colaMinimaxCopia.pop()
    
    solucion = []
    utilidad = resultado.getUtilidad()
    solucion.append(resultado.getHijo().getMapa())
    #while resultado.getHijo() != None:
     #   solucion.append(resultado.getMapa())
      #  resultado = resultado.getHijo()
    fin = time.time()

    #solucion.append(mapa)
    puntos = resultado.getHijo().getPuntosIA()
    print(puntos)
    return solucion, utilidad, fin-inicio, resultado.getHijo()

    

   

        


                


        
                

        




        



