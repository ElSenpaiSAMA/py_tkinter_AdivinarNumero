import random
import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu

root = tk.Tk()
root.title("Juego")
root.geometry("600x450")
nivel = 0
intentos = 10

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

def Dificultad(value):
    global nivel
    if value == "FÁCIL":
        nivel = 5
    elif value == "MEDIO":
        nivel = 10
    elif value == "DIFICIL":
        nivel = 100
    mos.config(text=f"Dificultad: {value} (Número entre 1 y {nivel})")

def Cerrar():
    root.destroy()

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

root.mainloop()

