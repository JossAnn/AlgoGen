import os
import tkinter as tk
from tkinter import ttk
import json

def submit():
    params = {
        "valueA": int(valueA.get()),
        "valueB": int(valueB.get()),
        "deltaX": float(deltaX.get()),
        "initialPopu": int(initialPopu.get()),
        "maxiPopu": int(maxiPopu.get()),
        "mutationIndiProba": float(mutationIndiProba.get()),
        "mutationGenProba": float(mutationGenProba.get()),
        "generationNumber": int(generationNumber.get())
    }
    print(json.dumps(params, indent=4))#se envia el json de parametros rescatado
    squaredParams.destroy()
    

squaredParams = tk.Tk()
squaredParams.title("Parametrizacion de Maximizacion")

#Valor de A
tk.Label(squaredParams, text="Valor A").grid(row=0, column=0)
valueA = tk.Entry(squaredParams)
valueA.grid(row=0, column=1)
#Valor de B
tk.Label(squaredParams, text="Valor B").grid(row=1, column=0)
valueB = tk.Entry(squaredParams)
valueB.grid(row=1, column=1)
#DeltaX
tk.Label(squaredParams, text="DeltaX").grid(row=2, column=0)
deltaX = tk.Entry(squaredParams)
deltaX.grid(row=2, column=1)
#Poblacion inicial
tk.Label(squaredParams, text="Poblacion Inicial").grid(row=4, column=0)
initialPopu = tk.Entry(squaredParams)
initialPopu.grid(row=4, column=1)
#Poblacion maxima
tk.Label(squaredParams, text="Poblacion Maxima").grid(row=5, column=0)
maxiPopu = tk.Entry(squaredParams)
maxiPopu.grid(row=5, column=1)
#Probabilidad de mutacion del individuo
tk.Label(squaredParams, text="Probabilidad de Mutacion del Individuo").grid(row=6, column=0)
mutationIndiProba = tk.Entry(squaredParams)
mutationIndiProba.grid(row=6, column=1)
#Probabilidad de mutacion del Gen
tk.Label(squaredParams, text="Probabilidad de mutacion del Gen").grid(row=7, column=0)
mutationGenProba = tk.Entry(squaredParams)
mutationGenProba.grid(row=7, column=1)

tk.Label(squaredParams, text="Numero de generaciones").grid(row=8, column=0)
generationNumber = tk.Entry(squaredParams)
generationNumber.grid(row=8, column=1)

# Valores predeterminados
valueA.insert(0, "2")
valueB.insert(0, "9")
deltaX.insert(0, "1.0")
initialPopu.insert(0, "9")
maxiPopu.insert(0, "27")
mutationIndiProba.insert(0, "10")
mutationGenProba.insert(0, "50")
generationNumber.insert(0,"3")

submit_button = tk.Button(squaredParams, text="Submit", command=submit)
submit_button.grid(row=9, column=0, columnspan=2)

squaredParams.mainloop()
