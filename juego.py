import random
import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu
import pygame

pygame.mixer.init()
root = tk.Tk()
root.title("Juego")
root.geometry("600x450")
nivel = 0
intentos = 10
pausa = True

def juego():
    global nivel
    global intentos
    try:
        adivinar = random.randint(1, nivel)
        num = int(numero.get())
        if num < 1 or num > nivel:
            mostrar = f"Número inválido, por favor ingrese un número entre 1 y {nivel}."
            mos.config(text=mostrar)
        else:
            intentos -=1
            if num == adivinar:
                mostrar = f"Has Adivinado el número: {adivinar}"
                mos.config(text=mostrar)
                botonCerrar = tk.Button(root, text="CERRAR", command=Cerrar)
                botonCerrar.pack(pady=15)
                boton.config(state=tk.DISABLED)
            elif intentos == 0:
                mostrar = f"Has alcanzado el máximo de intentos. El número era: {adivinar}"
                mos.config(text=mostrar)
                boton.config(state=tk.DISABLED)
                botonCerrar = tk.Button(root, text="CERRAR", command=Cerrar)
                botonCerrar.pack(pady=15)
            else:
                mostrar = f"No has Adivinado. Te quedan  {intentos} intentos. El número era: {adivinar}."
                mos.config(text=mostrar)

    except ValueError:
        messagebox.showwarning("Atención", "ERROR")

#dificultades
def Dificultad(value):
    global nivel
    if value == "FÁCIL":
        nivel = 5
    elif value == "MEDIO":
        nivel = 10
    elif value == "DIFICIL":
        nivel = 100
    mostrar = f"Has seleccionado la dificultad {value}, adivina un numero entre 0 y {nivel}"
    mos.config(text=mostrar)

#funcion para cerrar el juego
def Cerrar():
    root.destroy()
#musica
def musica():
    global pausa
    if pausa:
        pygame.mixer.music.load("./contenido/hola.mp3")
        pygame.mixer.music.play(loops=0)
        musi.config(text="Pausa")
        pausa = False
    else:
        pygame.mixer.music.pause()
        musi.config(text="DIVIERTETE :)")
        pausa = True

#configuración
niveles = ["FÁCIL", "MEDIO", "DIFICIL"]
selected_option = StringVar()
selected_option.set(niveles[0])
dificultad_menu = OptionMenu(root, selected_option, *niveles, command=Dificultad)
dificultad_menu.pack(pady=10)
mensaje = tk.Label(root, text="Introduce un número:", font=("Helvetica", 12))
mensaje.pack(pady=10)
numero = tk.Entry(root, width=30)
numero.pack(pady=10)
boton = tk.Button(root, text="JUGAR", command=juego)
boton.pack(pady=15)
mos = tk.Label(root, text="", font=("Helvetica", 12))
mos.pack(pady=20)
musi = tk.Button(root, text="DIVIERTETE :)", command=musica)
musi.pack(pady=35)

root.mainloop()

