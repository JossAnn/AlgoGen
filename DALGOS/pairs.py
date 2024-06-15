"""import json
import random

def umb(): 
    umbral = random.randint(0,100)
    if umbral <50: return 0
    else: return 1

def pairing(population):
    # Cargar parámetros del archivo JSON
    jsonParamsPath = "jsons/params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)
    maxiPopu = params["maxiPopu"]
        
    pairedPopulation = []
    
    # Generar parejas
    for i, individual1 in enumerate(population):
        for j, individual2 in enumerate(population):
            if i != j and umb == 1:
                pairedPopulation.append([individual1, individual2])
                indies = len(pairedPopulation) *2
                if (indies) > maxiPopu:
                    return pairedPopulation[:-1]  # Si se excede el máximo, eliminar la última pareja
    
    return pairedPopulation""
    
import random

def umbral():
    return random.randint(0, 1)

def pairing(population):
    pairedPopulation = []
    for i, individual1 in enumerate(population):
        for j, individual2 in enumerate(population):
            if i < j and umbral() == 1:  # Llamar a la función umb() una vez
                pairedPopulation.append([individual1, individual2])
    return pairedPopulation

""" 
import random

def pairing(population):
    pairedPopulation = []
    # Calcular el número de parejas (10% de la población)
    num_pairs = int(len(population) * 0.17)
    # Seleccionar aleatoriamente el 10% de la población para formar parejas
    paired_individuals = random.sample(population, num_pairs * 2)  # Se multiplican por 2 para formar parejas
    # Formar parejas con los individuos seleccionados
    for i in range(0, len(paired_individuals)-1, 2):
        pairedPopulation.append([paired_individuals[i], paired_individuals[i + 1]])
    return pairedPopulation
