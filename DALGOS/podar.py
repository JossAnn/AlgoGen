import json

#funcion para limitar la poblacion del algoritmo genetico
def poda(cursedPopulation):
    jsonParamsPath = "jsons\params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)
    """ Instrucciones:
    Dados los valores del fitness, generar clases, luego por clase mantener algunos individuos de manera aleatoria.
    Nota:
    el parametro que la funcion poda(cursedPopulation) recibe, se ve de la siguiene manera:
    [[7, '0000111', 27.0, -7.887747835813577], [51, '0110011', 71.0, -21.94061369979102], [14, '0001110', 34.0, -28.851389342676576], ...]
    """
    maxiPopu = params["maxiPopu"]
    print(maxiPopu)
    
    return cursedPopulation