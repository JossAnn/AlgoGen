import json
import random
import math

def crossOver(pairedPopulation):
    jsonParamsPath = "jsons/params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)

    valueA = params["valueA"]
    valueB = params["valueB"]
    deltaX = params["deltaX"]
    newPopulation = []
    noPts = int(((valueB - valueA) / deltaX) + 1)
    bitsNum = math.ceil(math.log2(noPts))

    for pair in pairedPopulation:
        individuo1, individuo2 = pair
        puntosCruza = random.randint(1, bitsNum)
        posiciones = random.sample(range(bitsNum), puntosCruza)
        bits1 = list(individuo1[1])
        bits2 = list(individuo2[1])
        
        for pos in posiciones:
            bits1[pos], bits2[pos] = bits2[pos], bits1[pos]
        newBitsChain1 = ''.join(bits1)
        newBitsChain2 = ''.join(bits2)

        indexS = [int(newBitsChain1, 2), int(newBitsChain2, 2)]
        binIndexS = [newBitsChain1, newBitsChain2]
        xS = [valueA + index * deltaX for index in indexS]
        fxS = [x * math.cos(x) for x in xS]
        individuos = [[index, binIndex, x, fx] for index, binIndex, x, fx in zip(indexS, binIndexS, xS, fxS)]
        newPopulation.extend(individuos)
        
        for pair in pairedPopulation:
            newPopulation.extend(pair)
            
    return newPopulation                                                                                            

""" 
import json
import random
import math

def crossOver(pairedPopulation):
    jsonParamsPath = "jsons/params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)

    valueA = params["valueA"]
    valueB = params["valueB"]
    deltaX = params["deltaX"]
    
    newPopulation = []
    
    noPts = int(((valueB - valueA) / deltaX) + 1)
    bitsNum = math.ceil(math.log2(noPts))

    for pair in pairedPopulation:
        individuo1, individuo2 = pair
        # Generar puntos de cruza
        puntosCruza = random.randint(1, bitsNum) # puntosCruza = 2
        # Seleccionar posiciones aleatorias para intercambiar
        posiciones = random.sample(range(bitsNum), puntosCruza)  # posiciones = [1, 3]
        #Se des-hacen las cadenas en listas
        bits1 = list(individuo1[1])# '101' -> '0101' con bitsNum = 4 
        bits2 = list(individuo2[1])
        
        for pos in posiciones:
            bits1[pos], bits2[pos] = bits2[pos], bits1[pos] #intercambio de bits por posisiones
            
        #Re-hacer de listas a cadenas
        newBitsChain1 = ''.join(bits1)
        newBitsChain2 = ''.join(bits2)

        # Rellenar los nuevos individuos (las mutaciones, hay dos mutaciones por cada pareja,)
        indexS = [int(newBitsChain1, 2), int(newBitsChain2, 2)] #calcular el binario a entero
        binIndexS = [newBitsChain1, newBitsChain2]
        xS = [valueA + index * deltaX for index in indexS]
        fxS = [x * math.cos(x) for x in xS]
        individuos = [[index, binIndex, x, fx] for index, binIndex, x, fx in zip(indexS, binIndexS, xS, fxS)]#construir

        #los mutados a cursedPopulation
        newPopulation.extend(individuos)
        #los originales a cursedPopulation
        for pair in pairedPopulation:
            newPopulation.extend(pair)
            
    return newPopulation
"""
