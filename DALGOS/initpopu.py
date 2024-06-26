import math
import random
import json

def initPopu():
    jsonParamsPath = "jsons\\params.json"
    with open(jsonParamsPath, "r") as json_file:
        params = json.load(json_file)

    valueA = params["valueA"]
    valueB = params["valueB"]
    deltaX = params["deltaX"]
    initialPopu = params["initialPopu"]
    
    noPts = int(((valueB - valueA) / deltaX) + 1)
    nExpo = math.ceil(math.log2(noPts))
    
    indexS = [random.randint(0, noPts-2) for _ in range(initialPopu)]
    
    binIndexS = [format(index, f'0{nExpo}b') for index in indexS]
    
    xS = [valueA + index * deltaX for index in indexS]
    
    fxS = [x * math.cos(x) for x in xS]
    
    individuos = [[index, binIndex, x, fx] for index, binIndex, x, fx in zip(indexS, binIndexS, xS, fxS)]
   #individuos = [[1, "001", 3.0, -2.96997748]]
    return individuos

""" population SE VE ASI:
[
    [3, '011', 5.0, 1.4183109273161312], 
    [1, '001', 3.0, -2.9699774898013365], 
    [4, '100', 6.0, 5.761021719902196], 
    [4, '100', 6.0, 5.761021719902196], 
    [3, '011', 5.0, 1.4183109273161312], 
    [4, '100', 6.0, 5.761021719902196], 
    [0, '000', 2.0, -0.8322936730942848], 
    [3, '011', 5.0, 1.4183109273161312], 
    [5, '101', 7.0, 5.277315780403132]
]
"""
#El ciclo se inicia aqui, pero debe ser "reconectado" desde main para que este codigo no se vuelva a tocar (params.py & initpopu.py)