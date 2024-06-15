import os
import tkinter as tk
from tkinter import ttk
import json

def submit(paramsWindow, entries):
    params = {
        "valueA": int(entries['valueA'].get()),
        "valueB": int(entries['valueB'].get()),
        "deltaX": float(entries['deltaX'].get()),
        "initialPopu": int(entries['initialPopu'].get()),
        "maxiPopu": int(entries['maxiPopu'].get()),
        "mutationIndiProba": float(entries['mutationIndiProba'].get()),
        "mutationGenProba": float(entries['mutationGenProba'].get()),
        "generationNumber": int(entries['generationNumber'].get())
    }

    # Crear carpeta 'jsons' si no existe
    os.makedirs('jsons', exist_ok=True)

    # Escribir los parámetros en un archivo JSON
    with open('jsons/params.json', 'w') as json_file:
        json.dump(params, json_file, indent=4)

    json.dumps(params, indent=4) # Se envía el json de parámetros rescatado
    paramsWindow.destroy()

def ventanaParametral():
    squaredParams = tk.Tk()
    squaredParams.title("Parametrización")
    
    entries = {}
    
    # Valor de A
    tk.Label(squaredParams, text="Valor A").grid(row=0, column=0)
    entries['valueA'] = tk.Entry(squaredParams)
    entries['valueA'].grid(row=0, column=1)
    # Valor de B
    tk.Label(squaredParams, text="Valor B").grid(row=1, column=0)
    entries['valueB'] = tk.Entry(squaredParams)
    entries['valueB'].grid(row=1, column=1)
    # DeltaX
    tk.Label(squaredParams, text="DeltaX").grid(row=2, column=0)
    entries['deltaX'] = tk.Entry(squaredParams)
    entries['deltaX'].grid(row=2, column=1)
    # Población inicial
    tk.Label(squaredParams, text="Población Inicial").grid(row=4, column=0)
    entries['initialPopu'] = tk.Entry(squaredParams)
    entries['initialPopu'].grid(row=4, column=1)
    # Población máxima
    tk.Label(squaredParams, text="Población Máxima").grid(row=5, column=0)
    entries['maxiPopu'] = tk.Entry(squaredParams)
    entries['maxiPopu'].grid(row=5, column=1)
    # Probabilidad de mutación del individuo
    tk.Label(squaredParams, text="Probabilidad de Mutación del Individuo x/100").grid(row=6, column=0)
    entries['mutationIndiProba'] = tk.Entry(squaredParams)
    entries['mutationIndiProba'].grid(row=6, column=1)
    # Probabilidad de mutación del Gen
    tk.Label(squaredParams, text="Probabilidad de mutación del Gen x/100").grid(row=7, column=0)
    entries['mutationGenProba'] = tk.Entry(squaredParams)
    entries['mutationGenProba'].grid(row=7, column=1)
    # Número de generaciones
    tk.Label(squaredParams, text="Número de generaciones").grid(row=8, column=0)
    entries['generationNumber'] = tk.Entry(squaredParams)
    entries['generationNumber'].grid(row=8, column=1)
    
    # Valores predeterminados
    entries['valueA'].insert(0, "20")
    entries['valueB'].insert(0, "90")
    entries['deltaX'].insert(0, "1.0")
    entries['initialPopu'].insert(0, "20")
    entries['maxiPopu'].insert(0, "50")
    entries['mutationIndiProba'].insert(0, "10")
    entries['mutationGenProba'].insert(0, "50")
    entries['generationNumber'].insert(0, "30")
    
    submit_button = tk.Button(squaredParams, text="Submit", command=lambda: submit(squaredParams, entries))
    submit_button.grid(row=9, column=0, columnspan=2)
    
    squaredParams.mainloop()

