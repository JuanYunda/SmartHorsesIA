#Proyecto SmartHorseIA
#Elaborado por:
#Mauricio Carrillo - 2024092
#Juan Esteban Mazuera - 2043008
#Sheilly Ortega - 2040051

import tkinter as tk
import easygui
import time
from PIL import Image, ImageTk
import easygui as eg
import numpy as np
from horse import Horse


botones = None
flag = True
global tipo_busqueda

# Función para dibujar el mapa en la ventana
def draw_map(canvas, map_data):
    global images
    
    # Dibujar cada celda en el canvas con la imagen correspondiente
    filas = len(map_data)
    colum = len(map_data[0])
    for row_idx in range(filas):
        for col_idx in range(colum):
            x1 = col_idx * CELL_SIZE
            y1 = row_idx * CELL_SIZE
            canvas.create_image(x1, y1, image=images[int(map_data[row_idx][col_idx])], anchor='nw')

# Función que imprime la solución que retorna la función de busqueda
def imprimir():
    # Actualizar el ciclo for para que recorra la lista de soluciones
    for i in reversed(solucion):
        # Definir el mapa que se desea mostrar
        map_data = i

        # Dibujar el mapa en el canvas
        draw_map(canvas, map_data)
        ventana.update()
        time.sleep(0.5)
    
# Actualizar los valores de las etiquetas
def actualizarValores(expand, prof, tiem, cost):
    etiqueta_costo.config(text='Costo de la solución: ' + str(cost))

#reconfigura los elementos dentro de la interfaz (funcion que sirve si se desea realizar mas de un tipo de busqueda en la misma ejecución)
def cargar_mapa():
    global matrizInicial
    global solucion

    mostrar_interfaz()

    archivo = eg.fileopenbox(msg='Seleccione el nuevo mapa',
                            title='Seleccion de mapa',
                            multiple=False)


    if archivo is not None:
        mapa = open(archivo, 'r')
        matrizInicial = np.loadtxt(mapa, dtype='i', delimiter=' ')
        mapa.close()

        # Limpiar la solución anterior
        solucion = []

        # Dibujar el nuevo mapa en el lienzo
        draw_map(canvas, matrizInicial)

        # Actualizar la interfaz
        ventana.update()

#funcion asociada al boton de salir, que cierra la ventana
def cerrar_programa():
    ventana.destroy()

# Función para cambiar la dificultad del juego
def cambiar_variable(valor):
    global dificultad
    global profundidadMaxima
    global minimo
    global maximo 
    dificultad = valor
    if dificultad == 1:
        profundidadMaxima = 3
    elif dificultad == 2:
        profundidadMaxima = 5
    elif dificultad == 3:
        profundidadMaxima = 7
    maximo, minimo = 1000, -1000

# Función que muestra la interfaz flotante para seleccionar la dificultad
def mostrar_interfaz():
    respuesta = easygui.buttonbox("Seleccione la dificultad:", choices=["Principiante", "Amateur", "Experto"])
    if respuesta == "Principiante":
        cambiar_variable(1)
    elif respuesta == "Amateur":
        cambiar_variable(2)
    elif respuesta == "Experto":
        cambiar_variable(3)

def minimax(profundidad, nodoIndice,maximizarJugador,valores,alfa,beta):
    if profundidad == profundidadMaxima:
        return valores[nodoIndice]
    
    if maximizarJugador:
        mejor = minimo
        for i in range(0,8):
            valores = minimax(profundidad + 1, nodoIndice * 2 + i,)
    

# Crear la ventana
ventana = tk.Tk()
ventana.title("Smart Horses")
ventana.resizable(False, False)  # Desactivar la redimensión de la ventana
# Cambiar el color de fondo de la ventana a azul
ventana.configure(bg="white")

# Crear el contenedor para los botones
contenedor_puntajes = tk.Frame(ventana)
contenedor_puntajes.pack(side='top', padx=5, pady=5)
# Boton "Cargar Nuevo Mapa"
btn_cargar_mapa = tk.Button(contenedor_puntajes, text='Puntos', command=cargar_mapa, bg="blue")
btn_cargar_mapa.pack(side='left', padx=(0, 200))
# Crear el botón "Cerrar"
btn_cerrar = tk.Button(contenedor_puntajes, text="Puntos", command=cerrar_programa, bg="red")
btn_cerrar.pack(side="left", padx=(200, 0))


# Crear el canvas para dibujar el mapa
CELL_SIZE = 50
canvas = tk.Canvas(ventana, width=400, height=400, bg='gray')
canvas.pack()

# Cargar las imágenes que deseas mostrar en la interfaz
img_1 = Image.open('casillas/1.png') #casilla de 1 punto
img_2 = Image.open('casillas/2.png') #casilla de 2 punto
img_3 = Image.open('casillas/3.png') #casilla de 3 punto
img_4 = Image.open('casillas/4.png') #casilla de 4 punto
img_5 = Image.open('casillas/5.png') #casilla de 5 punto
img_6 = Image.open('casillas/6.png') #casilla de 6 punto
img_7 = Image.open('casillas/7.png') #casilla de 7 punto
img_casilla = Image.open('casillas/fondo.png') #casilla libre
img_caballoIa = Image.open('casillas/ia.png') #caballo blanco de la IA
img_caballoJugador = Image.open('casillas/jugador.png') #caballo negro del jugador
img_casillaValida = Image.open('casillas/valida.png') #casilla a la que se puede mover el caballo del jugador
    
# Escalar las imágenes a la dimensión de las celdas
img_1 = img_1.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_2 = img_2.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_3 = img_3.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_4 = img_4.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_5 = img_5.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_6 = img_6.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_7 = img_7.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_casilla = img_casilla.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_caballoIa = img_caballoIa.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_caballoJugador = img_caballoJugador.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_casillaValida = img_casillaValida.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
    
# Convertir las imágenes a un formato compatible con tkinter
img_1 = ImageTk.PhotoImage(img_1)
img_2 = ImageTk.PhotoImage(img_2)
img_3 = ImageTk.PhotoImage(img_3)
img_4 = ImageTk.PhotoImage(img_4)
img_5 = ImageTk.PhotoImage(img_5)
img_6 = ImageTk.PhotoImage(img_6)
img_7 = ImageTk.PhotoImage(img_7)
img_casilla = ImageTk.PhotoImage(img_casilla)
img_caballoIa = ImageTk.PhotoImage(img_caballoIa)
img_caballoJugador = ImageTk.PhotoImage(img_caballoJugador)
img_casillaValida = ImageTk.PhotoImage(img_casillaValida)

# Definir las imagenes para cada valor en el mapa
images = {
    0: img_casilla,
    1: img_1,
    2: img_2,
    3: img_3,
    4: img_4,
    5: img_5,
    6: img_6,
    7: img_7,
    8: img_caballoIa,
    9: img_caballoJugador,
    10: img_casillaValida,
}

solucion = []

mostrar_interfaz()

archivo = eg.fileopenbox(msg='Seleccione el mapa',
                        title='Seleccion de mapa',
                        multiple=False,
                        )
     
mapa = open(archivo, 'r')
matrizInicial = np.loadtxt(mapa, dtype='i', delimiter=' ')

draw_map(canvas, matrizInicial)

for i in range(len(images)-1):
    images.pop(i)

# Mostrar la ventana
print("finalizado")
ventana.mainloop()
