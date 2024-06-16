import json
import matplotlib.pyplot as plt
import os

# Recibe la poblacion
def evaluateFitness(population):
    # Crear directorio para guardar las graficas
    graphicDir = 'graphicGenerations'
    if not os.path.exists(graphicDir):
        os.makedirs(graphicDir)

    # Extraer valores fx
    fxValues = [individuo[3] for individuo in population]
    generacion = len(os.listdir(graphicDir)) + 1

    # Graficar valores fx
    plt.figure(figsize=(10, 6))
    plt.plot(fxValues, 'bo', label='fx values', markersize=4)  # Puntos
    plt.plot(fxValues, 'b-', alpha=0.5)  # Línea que conecta los puntos
    plt.title(f'Generación {generacion}', fontsize=16, fontweight='bold')
    plt.xlabel('Individuo', fontsize=14)
    plt.ylabel('fx', fontsize=14)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    #segun optimiza la grafica
    plt.tight_layout()

    # Guardar grafica
    graphicName = f'{graphicDir}/generation_{generacion}.png'
    plt.savefig(graphicName, dpi=300)
    plt.close()

    # Seleccionar el valor mas alto, bajo y promedio de 'fx'
    fxMax = max(fxValues)
    fxMin = min(fxValues)
    fxAvg = sum(fxValues) / len(fxValues)

    # Encontrar los individuos correspondientes
    maxIndividuo = next(ind for ind in population if ind[3] == fxMax)
    minIndividuo = next(ind for ind in population if ind[3] == fxMin)
    avgIndividuo = min(population, key=lambda ind: abs(ind[3] - fxAvg))

    selectedIndivs = {
        "fxMax": maxIndividuo,
        "fxMin": minIndividuo,
        "fxAvg": avgIndividuo
    }

    # Todo pa abajo guarda los 3 valores rescatados de cada generacion en un JSON
    jsonsDirPath = 'jsons'
    if not os.path.exists(jsonsDirPath):
        os.makedirs(jsonsDirPath)

    jsonFilePath = os.path.join(jsonsDirPath, "GeneJson.json")

    # Leer contenido existente del archivo
    if os.path.exists(jsonFilePath):
        with open(jsonFilePath, 'r') as jsonFile:
            try:
                data = json.load(jsonFile)
                if not isinstance(data, list):
                    data = [data]
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Agregar nuevos datos a la lista existente
    data.append(selectedIndivs)

    # Guardar la lista actualizada en el archivo JSON
    with open(jsonFilePath, 'w') as jsonFileIs:
        json.dump(data, jsonFileIs, indent=4)

    #print(f"Datos añadidos al JSON: {jsonFilePath}")



"""   
FORMATO DEL GeneJson.json
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
    ... (cada ejecucion del fitness arroja un nuevo json con los 3 individuos)
]
"""