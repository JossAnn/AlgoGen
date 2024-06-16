import os
import cv2
import json
import matplotlib.pyplot as plt
import shutil
import tkinter as tk
from tkinter import messagebox

def videoEnsambler(graphicGens, videoPath):
    images = [img for img in os.listdir(graphicGens) if img.endswith(".png")]
    images.sort()  #pa juntarlas Aunque lo hace un poco raro pq en el video no salen como tal en orden
    
    frame = cv2.imread(os.path.join(graphicGens, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(videoPath, cv2.VideoWriter_fourcc(*'mp4v'), 3, (width, height))#propiedades del video
    
    for image in images:
        video.write(cv2.imread(os.path.join(graphicGens, image)))
    
    video.release()

def generationsGraphic(jsonsPath, graphicPath):
    #grafica de evolucion
    with open(jsonsPath, 'r') as f:
        data = json.load(f)
    
    fxMax = [entry["fxMax"][-1] for entry in data]
    fxMin = [entry["fxMin"][-1] for entry in data]
    fxAvg = [entry["fxAvg"][-1] for entry in data]
    
    plt.figure()
    plt.plot(fxMax, color='green', linestyle='-', label='fxMax')
    plt.plot(fxMin, color='red', linestyle='-', label='fxMin')
    plt.plot(fxAvg, color='blue', linestyle='-', label='fxAvg')
    
    plt.title('Evolución de Generaciones', fontsize=16)
    plt.xlabel('Generación', fontsize=14)
    plt.ylabel('Valor de Función', fontsize=14)
    
    plt.legend(loc='best', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    
    plt.tight_layout()
    plt.savefig(graphicPath, dpi=300)
    plt.close()

def terminator(jsons, graphicGens,__pycache__):
    #Aqui se destruye si no se quiere guardar
    def on_closing():
        if messagebox.askyesno("Eliminar carpetas", "¿Desea eliminar las carpetas?\n-> jsons\n-> jsonsgraphicGens\n-> __pycache__\n\nBorrarlas o mantenerlas no afectara la creacion\ndel video ni de la grafica de generaciones"):
            shutil.rmtree(jsons)
            shutil.rmtree(graphicGens)
            shutil.rmtree(__pycache__)
            root.destroy()
        else:
            root.destroy()
    
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.after(0, on_closing)
    root.mainloop()

def activate():
    #activate genera el video, la grafica de evolucion y destruye si se decide
    graphicGens = "graphicGenerations"
    jsons = "jsons"
    __pycache__ = "__pycache__"
    videoPath = os.path.join("Video_De_Generaciones.mp4")
    jsonsPath = os.path.join(jsons, "GeneJson.json")
    graphicPath = os.path.join("Grafica_De_Evolucion.png")
    
    videoEnsambler(graphicGens, videoPath)
    generationsGraphic(jsonsPath, graphicPath)
    terminator(jsons, graphicGens, __pycache__)

