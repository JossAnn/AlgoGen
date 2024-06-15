
"""
1.- Debe generar un video con todas las imagenes .png que ya se encuentran en una carpeta llamada "graphicGenerations" y guardarlo en la misma carpeta con el nombre "video_final"
2.- Debe generar una grafica con los valores extraidos del archivo "GeneJson.json" que se encuentra dentro de la carpeta "jsons".
    Notese que en el archivo se encuentran datos estructurados de la siguiente manera:
    [
        {
            "fxMax": [ 55, "0110111", 75.0, 69.1313452293562 ],
            "fxMin": [ 65, "1000001", 85.0, -83.67201468849356 ],
            "fxAvg": [ 16, "0010000", 36.0, -4.606692826586569 ]
        },
        {
            "fxMax": [ 42, "0101010", 62.0, 41.75744406406235 ],
            "fxMin": [ 108, "1101100", 128.0, -88.69066520578113 ],
            "fxAvg": [ 32, "0100000", 52.0, -8.475520601376685 ]
        },
        ...
    ]
    Por lo tanto la grafica debe contar con tres lineas: 
        verde para seguir el comportamiento de la ultima posision de "fxMax"
        roja para seguir el comportamiento de la ultima posision de "fxMin"
        amarilla para seguir el comportamiento de la ultima posision de "fxAvg"
        
3.- Debe lanzar un cuadro de alerta que pregunte si se desean guardar o los datos o no.
    si se elige que no se guarden o si no se recibe respuesta positiva (que la ventana se cierre), se deben eliminar las carpetas "jsons" y "graphicGenerations"
"""

import os
import cv2
import json
import matplotlib.pyplot as plt
import shutil
import tkinter as tk
from tkinter import messagebox

def videoEnsambler(graphicGens, videoPath):
    images = [img for img in os.listdir(graphicGens) if img.endswith(".png")]
    images.sort()  # Aseguramos que las imágenes se ordenen correctamente
    
    frame = cv2.imread(os.path.join(graphicGens, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(videoPath, cv2.VideoWriter_fourcc(*'mp4v'), 1, (width, height))
    
    for image in images:
        video.write(cv2.imread(os.path.join(graphicGens, image)))
    
    video.release()

def generationsGraphic(jsonsPath, graphicPath):
    with open(jsonsPath, 'r') as f:
        data = json.load(f)
    
    fxMax = [entry["fxMax"][-1] for entry in data]
    fxMin = [entry["fxMin"][-1] for entry in data]
    fxAvg = [entry["fxAvg"][-1] for entry in data]
    
    plt.figure()
    plt.plot(fxMax, color='green', label='fxMax')
    plt.plot(fxMin, color='red', label='fxMin')
    plt.plot(fxAvg, color='yellow', label='fxAvg')
    plt.legend()
    plt.savefig(graphicPath)
    plt.close()

def terminator(jsons, graphicGens):
    def on_closing():
        if messagebox.askyesno("Guardar datos", "¿Desea guardar los datos?"):
            root.destroy()
        else:
            shutil.rmtree(jsons)
            shutil.rmtree(graphicGens)
            root.destroy()
    
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.after(0, on_closing)
    root.mainloop()

def activate():
    graphicGens = "graphicGenerations"
    jsons = "jsons"
    videoPath = os.path.join(graphicGens, "video_final.mp4")
    jsonsPath = os.path.join(jsons, "GeneJson.json")
    graphicPath = os.path.join(jsons, "output_graph.png")
    
    videoEnsambler(graphicGens, videoPath)
    generationsGraphic(jsonsPath, graphicPath)
    terminator(jsons, graphicGens)

activate()
